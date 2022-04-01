import requests

def generate_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

def get_username():
    response = generate_request('https://randomuser.me/api')
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')
 

def get_apidolar():
    response = generate_request('https://mindicador.cl/api')
    if response:
       user = response.get('dolar')
       return user
 