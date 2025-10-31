import os
import requests

# Usa a API de testes que realmente existe
EXTERNAL_BASE = os.getenv("EXTERNAL_API_URL", "https://jsonplaceholder.typicode.com")


def fetch_all():
    url = f"{EXTERNAL_BASE}/posts"
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()


def fetch_by_id(item_id: int):
    url = f"{EXTERNAL_BASE}/posts/{item_id}"
    resp = requests.get(url, timeout=5)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def create(data: dict):
    url = f"{EXTERNAL_BASE}/posts"
    resp = requests.post(url, json=data, timeout=5)
    if resp.status_code >= 400:
        return None
    return resp.json()
