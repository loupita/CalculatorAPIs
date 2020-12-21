import requests
import json

def test_checkPostedData():
    url = 'localhost:8080/add'

    #Additionnal headers
    headers = {'content-type':'application/json'}

    #Body
    payload = {'x':1, 'y':2}

    resp = requests.post(url, headers=headers, data=json.dump(payload, indent=4))
    assert resp.status_code == 200
