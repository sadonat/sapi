import requests
from rich import print
import utils


def test(name, file):
    collection_data = utils.collection_load(file)
    response = utils.run(name, collection_data)
    print(f"{response.request.method} {response.url} {response.elapsed.total_seconds() * 1000:.2f}ms {f"[bold green][{response.status_code}][/bold green]" if response.ok else f"[bold red][{response.status_code}][/bold red]"} ")
    print(response.json())

def multi_test(file):
    collection_data = utils.collection_load(file)
    print(f"Testing {collection_data['base_url']}")
    with open('sapi_report.md', 'w') as report:
        report.write(f"# TESTING REPORT FOR {collection_data['base_url']}\n")
        for edp_name in collection_data['endpoints']:
            response = utils.run(edp_name, collection_data)
            res_short_url = response.url.replace(collection_data['base_url'], "")
            res_method = response.request.method
            res_time = f"{response.elapsed.total_seconds() * 1000 : .2f}ms"
            res_json = response.json()
            res_stat_code = response.status_code
            req_json = response.request.body
            report.write(f"\n## [{res_method}] {res_short_url}\n")
            report.write(f"time: {res_time}\nRequest body:\n```json\n{req_json}\n```\nResponse:\n```json\n{res_json}\n```\n")
            print(f"{res_method} {res_short_url} {res_time} {f"[bold green][{res_stat_code}][/bold green]" if response.ok else f"[bold red][{res_stat_code}][/bold red]"} ")

