import pytest
import requests

url = 'http://python-data-service:5000'
headers = {
    "Content-Type": "application/json"}



def test_post_api():
    input_data = '{"student_name":"arora","student_id":"id","student_email":"email","student_phone":"phone","student_class":"class"}'
    x = requests.post(url + '/postdata', data=input_data, headers=headers)
    assert x.status_code == 200


def test_get_api():
    x = requests.get(url + '/getdata', headers=headers)
    assert x.status_code == 200


def test_get_by_name_api():
    x = requests.get(url + '/getdatabyname/arora', headers=headers)
    assert x.status_code == 200
    print(x.text)


def test_update_by_name():
    input_data = '{"student_name":"ishan","student_id":"id","student_email":"email","student_phone":"phone","student_class":"class"}'
    x = requests.put(url + '/updatedatabyname/arora', data=input_data, headers=headers)
    assert x.status_code == 200
    print(x.text)


def test_delete_by_name():
    x = requests.delete(url + '/deletedatabyname/ishan', headers=headers)
    assert x.status_code == 200
    print(x)
