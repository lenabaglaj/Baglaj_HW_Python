import requests
from conftest import base_url, Token, Token_negative, ID_Project, projectID, projectID_negative

def test_auth_you():
    you = {
        'login': 'm29712461@gmail.com',
        'password': 'Alina2011',
        'name': 'поток_102.2'
}
    resp = requests.post(base_url + '/api-v2/auth/companies', json=you,
    timeout=10)
    assert resp.status_code == 200

    resp = requests.get(base_url + '/api-v2/projects', json=you, timeout=10)
    body = resp.json()