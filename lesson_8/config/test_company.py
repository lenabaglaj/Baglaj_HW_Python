import requests
import pytest
from config.conftest import base_url, Token, Token_negative, ID_Project, projectID, projectID_negative

@pytest.fixture
def create_project():
    return test_create_new_project_positive()

def test_create_new_project_positive():
    payload = {
        'title': 'ГосУслуги1000',
        'users': {
            '1f6234cf-e8ca-4731-b01f-1388de02021d': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Token}'
}
    resp = requests.post(f'{base_url}/api-v2/projects', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 201


def test_create_new_project_negative():
    payload = {
        'title': '   ',
        'users': {
            '1f6234cf-e8ca-4731-b01f-1388de02021d': 'admin'
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {Token_negative}'
}
    resp = requests.post(f'{base_url}/api-v2/projects', json=payload, headers=headers)
    response_data = resp.json()
    assert 'id' in response_data
    assert resp.status_code == 201