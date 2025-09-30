import pytest
import requests

base_url = "http://5.101.50.27:8000"

def get_company_list():
    resp = requests.get(base_url + '/company/list')
    return resp.json()

def test_get_companies():
    resp = requests.get(base_url + '/company/list')
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0

def test_get_active_companies():
    resp = requests.get(base_url + '/company/list')
    full_list = resp.json()

    # Получить список активных компаний
    resp = requests.get(base_url + '/company/list?active=true')
    filtered_list = resp.json()

    # Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)

# Получить список активных компаний
    my_params = {'active' : 'true'}
    resp = requests.get(base_url+'/company/list', params=my_params)
    filtered_list = resp.json()

def test_add_new():
    #получить количество компаний
    resp = requests.get(base_url + '/company/list')
    body = resp.json()
    len_before = len(body)

    #создать новую компанию

    # получить количество компаний
    resp = requests.get(base_url + '/company/list')
    body = resp.json()
    len_after = len(body)