import logging

import binascii
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from petlib.ec import EcPt, EcGroup

logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

EPOCH = None

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


def number_to_string(number):
    number_to_bytes = number.to_bytes(10000, byteorder='little')
    byte_string = number_to_bytes.replace(b'\x00', b'')

    return byte_string.decode()


def change_back(gene, key):
    gene = int(gene)
    if gene != 0:
        gene = number_to_string(int(gene))

    key = abs(int(key))
    if key != 0:
        key = number_to_string(key)

    return gene, key


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify([
        change_back(q.gene, q.key)
        for q in Query.query.all()
    ])


@app.route('/epoch', methods=['GET'])
def info():
    return jsonify({
        'current_epoch': EPOCH,
    })


@app.route('/parameters', methods=['GET'])
def parameters():
    return jsonify({
        "nid": 731,
    })


@app.route('/end-epoch', methods=['POST'])
def end_epoch():
    global EPOCH
    epoch = request.json['epoch']
    queries = request.json['queries']

    if epoch != EPOCH:
        EPOCH = epoch
        Query.query.delete()
        db.session.commit()

    for q in queries:
        current = Query.query.get(int(q["id"]))

        if current:
            current.gene = str(int(current.gene) + int(q["gene"]))
            current.key = str(int(current.key) + int(q["key"]))
        else:
            new_query = Query(int(q["id"]), str(q["gene"]), str(q["key"]))
            db.session.add(new_query)
    db.session.commit()

    return 'Got queries'
