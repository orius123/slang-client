__author__ = 'orius123'

import argparse

parser = argparse.ArgumentParser(description='Run a Slang flow')
parser.add_argument('-f', '--flow_id',
                    help='a flow to run')
parser.add_argument('-cp', '--classpath',
                    help='classpath to run the flow in')
parser.add_argument('inputs', nargs='+', metavar='input')

args = parser.parse_args()
print args

inputs = dict([i.split("=") for i in args.inputs])

import json
import requests
import pprint
url = 'http://localhost:8080/executions'
data = {
    "classpath": args.classpath,
    "flowId": args.flow_id,
    "runInputs": inputs
}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
pprint.pprint(response.json())
