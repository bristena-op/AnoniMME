import requests

import urllib.parse


def get_parameters(url, path):
    parameters_path = urllib.parse.urljoin(url, path)
    r = requests.get(parameters_path)

    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Could not retrieve the parameters from the master server.")