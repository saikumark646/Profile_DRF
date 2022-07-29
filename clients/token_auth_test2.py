import requests
# to register new user
def clients():
    data = {'username': 'test123',
            'email': 'test@gmail.com',
            'password1': 'asdf@123',
            'password2': 'asdf@123'}
    # 
    response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',data = data)
    response_data =  response.json()

if __name__ == '__main__':
    clients()