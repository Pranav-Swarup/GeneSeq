import requests

ENSEMBL_REST = "https://rest.ensembl.org"

def get_json(endpoint):
    url = f"{ENSEMBL_REST}{endpoint}"
    headers = {"Content-Type": "application/json"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        print(f"ERR - Error fetching {url} | Status: {r.status_code}")
        return None

def get_text(endpoint):
    url = f"{ENSEMBL_REST}{endpoint}"
    headers = {"Content-Type": "text/plain"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text
    else:
        print(f"ERR - Error fetching {url} | Status: {r.status_code}")
        return None
