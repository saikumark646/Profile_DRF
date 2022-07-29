
import requests

def clients():
    credentials  = {'username': 'test1','password':'asdf@123'}
    #this will create token automatically
    response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',data=credentials )


    # token_h = 'Token 41a1497f781cd0117ec862bd751a7f41767c0a6d'
    # headers = {'Authorization':token_h}
    # response = requests.get('http://127.0.0.1:8000/api/profile/',headers = headers)
    #to check profile details 

    #print('status code:', response.status_code)
    response_data = response.json()
    #print(response_data)


if __name__ == '__main__':
    clients()


#check this have to runserver in one terminal and in the new terminal open clients folder and run python token_auth_test.py

