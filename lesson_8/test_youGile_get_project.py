import requests
import pytest

base_url = "https://ru.yougile.com"
Token = ""
ID_Project = "30b0edd0-2059-4461-b4da-5cd130b32ef0"
projectID = "d56ce9d4-9090-431d-8bcb-fddbbcaafdc3"
projectID_negative = "d56ce9d4-9090-431d-8bcb-fddbbcaafdc34"

@pytest.fixture
def get_project():
    return test_get_positive()

def test_get_positive():
    payload = {
        'title': 'ГосУслуги105MMMM',
        'users': {
            '1f6234cf-e8ca-4731-b01f-1388de02021d': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Token}'
    }
    resp = requests.get(f'{base_url}/api-v2/projects/{projectID}', json=payload, headers=headers)
    response_data = resp.json()
    assert 'error' in response_data
    assert resp.status_code == 401

def test_get_negative():
    payload = {
        'title': 'ГосУслуги105MMMM',
        'users': {
            '1f6234cf-e8ca-4731-b01f-1388de02021d': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Token}'
    }
    resp = requests.get(f'{base_url}/api-v2/projects/{projectID_negative}', json=payload, headers=headers)
    response_data = resp.json()
    assert 'error' in response_data
    assert resp.status_code == 401