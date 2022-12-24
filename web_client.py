import requests
from pprint import pprint
r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, type(r.text), r.json())
#response = requests.post('http://127.0.0.1:5000/users', data={
#    "name": "Daniil",
#    "surname": "Medvedev"
#    })
r = requests.post('http://127.0.0.1:5000/users', json={
    "id": 2,
    "name": "Daniil",
    "surname": "Medvedev"
    })
pprint(r.json())
r = requests.post('http://127.0.0.1:5000/users', json={
    "id": 4,
    "name": "Daniil",
    "surname": "Pop"
    })
pprint(r.json())
r = requests.put('http://127.0.0.1:5000/users', json={
    "id": 1,
    "name": "Thom",
    "surname": "Boy"
    })
pprint(r.json())
r = requests.delete('http://127.0.0.1:5000/users', json={
    "id": 0,
    "name": "Alex",
    "surname": "Turner"
    })
pprint(r.text)