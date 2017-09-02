# Project name

Server description here.

## Prerequisites

- Python 3.6 or higher


## Start local development

Create a local virtual environemnt for the python project to avoid version collisions between dependencies of different
projects and install the development dependencies.

    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt


## Running tests

Make sure the testing dependencies are installed
    
    source .env/bin/activate
    pip install -r requirements.test.txt
    
Running tests

    python -m pytest


## Running scripts

Set the PYTHONPATH, make sure you are in the src/client directory:
    export PYTHONPATH=$(pwd)

### NOTES

Convert EcPt to a value that can work with json:

    str(hexlify(<EcPt>.export()).decode("utf8"))

Convert json value to EcPt, we need to know the nid value to generated the eliptic curve group:

    EcPt.from_binary(binascii.unhexlify(str.encode(<json_value>)),  EcGroup(nid=<nid value>))