import requests

def post_add_entry():
    url = 'http://127.0.0.1:5000/drinks'
    json_data = {"name":"orange","description":"bitter"}
    print(url)
    print(json_data)
    response = requests.post(url, json=json_data, allow_redirects=True)
    print(response)

post_add_entry()