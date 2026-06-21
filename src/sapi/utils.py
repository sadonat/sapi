import yaml
from rich import print
import requests

def msg_error(text):
    print(f"[red]Error:[/red] {text}")
    exit(1)

def collection_load(file):
    with open(file, "r") as f:
        config = yaml.safe_load(f)
    return config

def dict_get(dictionary, name, default_value = None):
    return dictionary.get(name, default_value)

def dict_require(dictionary, name):
    result = dictionary.get(name)
    if(result == None):
        msg_error(f"Theres no item named {name}")
    else:
        return result


def run(name, collection_data):
    edp_base_url = dict_require(collection_data, 'base_url')
    edp_data = collection_data['endpoints'].get(name)
    if edp_data == None:
        msg_error(f"Could not find endpoint named {name}")
    edp_path = dict_require(edp_data, 'path')
    edp_method = dict_require(edp_data, 'method')
    edp_params = dict_get(edp_data, 'params')
    edp_url = f"{edp_base_url}{edp_path}"
    edp_headers = dict_get(edp_data, 'headers')
    edp_json = dict_get(edp_data, 'json')
    response = requests.request(method=edp_method, url=edp_url,params=edp_params, headers=edp_headers, json=edp_json)
    return response
