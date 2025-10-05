import requests
import pytest
from conftest import base_url, Token, Token_negative, ID_Project, projectID, projectID_negative


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
    resp = requests.put(f'{base_url}/api-v2/projects/{ID_Project}', json=payload, headers=headers, timeout=10)
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
    resp = requests.put(f'{base_url}/api-v2/projects/{ID_Pproject_negative}',
    json=payload, headers=headers, timeout=10)
    response_data = resp.json()
    assert 'error' in response_data
    assert resp.status_code == 404