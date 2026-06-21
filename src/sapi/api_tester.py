import requests
import collection_utility

def run(name, file):
    collection_data = collection_utility.load(file + ".yaml")
    print(collection_data['endpoints'][name])
