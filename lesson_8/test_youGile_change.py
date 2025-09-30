import requests
import pytest

base_url = "https://ru.yougile.com"
Token = ""
ID_Project = "30b0edd0-2059-4461-b4da-5cd130b32ef0"
ID_Project_negative = "30b0edd0-2059-4461-b4da-5cd130b32ef01"

@pytest.fixture
def redakt_project():
    return test_redakt_positive()

def test_redakt_positive():
    payload = {
        'title': 'ГосУслуги105MMMMffffff',
        'users': {
            '1f6234cf-e8ca-4731-b01f-1388de02021d': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Token}'
    }
    resp = requests.put(f'{base_url}/api-v2/projects/{ID_Project}', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 200

def test_redakt_negative():
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
    resp = requests.put(f'{base_url}/api-v2/projects/{ID_Project_negative}', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 401