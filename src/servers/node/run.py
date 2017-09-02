import logging
import urllib
import requests

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from .constants import EPOCH_MAX_COUNT, MASTER_URL, MASTER_END_EPOCH_PATH

logging.basicConfig(level=logging.DEBUG)

EPOCH = 0
EPOCH_CURRENT_COUNT = 0

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gene = db.Column(db.String(2048))
    key = db.Column(db.String(2048))

    def __init__(self, id, gene, key):
        self.id = id
        self.gene = gene
        self.key = key

    def __repr__(self):
        return '<Query %r %r %r>' % (self.id, self.gene, self.key)

db.create_all()


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify([str(q) for q in Query.query.all()])


@app.route('/epoch', methods=['GET'])
def info():
    return jsonify({
        'current_epoch': EPOCH,
        'queries_max': EPOCH_MAX_COUNT,
        'queries_count': EPOCH_CURRENT_COUNT
    })


@app.route('/query', methods=['POST'])
def query():
    global EPOCH_CURRENT_COUNT
    gene = request.json['gene']
    key = request.json['key']

    # No more queries are accepted until the current epoch is sent to the master
    if EPOCH_CURRENT_COUNT >= EPOCH_MAX_COUNT:
        return 'Closing the current epoch', flask.ext.api.status.HTTP_503_SERVICE_UNAVAILABLE

    for i, (gene, key) in enumerate(zip(gene, key)):
        current = Query.query.get(i + 1)

        if current:
            current.gene = str(int(current.gene) + gene)
            current.key = str(int(current.key) + key)
        else:
            new_query = Query(i + 1, str(gene), str(key))
            db.session.add(new_query)
    db.session.commit()

    EPOCH_CURRENT_COUNT += 1

    if EPOCH_CURRENT_COUNT == EPOCH_MAX_COUNT:
        end_epoch()

    return 'Query received'


@app.route('/end-epoch', methods=['GET'])
def end_epoch():
    global EPOCH, EPOCH_CURRENT_COUNT

    queries = Query.query.all()

    payload = [
        {
            "id": q.id,
            "gene": q.gene,
            "key": q.key
        }
        for q in queries
    ]

    logging.debug(payload)

    end_epoch_path = urllib.parse.urljoin(MASTER_URL, MASTER_END_EPOCH_PATH)

    r = requests.post(end_epoch_path, json={'epoch': EPOCH, 'queries': payload})

    if r.status_code == 200:
        EPOCH += 1
        EPOCH_CURRENT_COUNT = 0
        Query.query.delete()
        db.session.commit()

        return 'Epoch send'
    else:
        logging.debug(r.status_code)
        logging.debug(r.content)

        return 'Issue ending epoch'
