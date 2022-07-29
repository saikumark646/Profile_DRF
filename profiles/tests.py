
import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer,ProfileStatusSerializer
from profiles.models import Profile,ProfileStatus

from rest_framework.authtoken.models import Token


class RegistrationTestCase(APITestCase):
    
    def test_registration(self):
        data = {'username' :'test1_case' ,'email':'adminn@gmail.com', 'password1':'asdf@123','password2':'asdf@123'}
        response = self.client.post('/api/rest-auth/registration/',data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        # asserEqual means checking two codes 

class ProfileViewSetTestCase(APITestCase):

    list_url  = reverse('profile-list')  
    detail_url  =reverse('profile-detail', kwargs = {'pk':1})

    def setUp(self):
        self.user = User.objects.create_user(username =  'sai' ,password = 'some_strong_psw')
        self.token = Token.objects.create(user = self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHENTIFICATION = 'Token'+self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get((self.list_url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user = None)
        response = self.client.get((self.list_url))
        self.assertEqual(response.status_code, status.HTTP_403_FORBEDDEN)        

    def test_profile_detail_retrieve(self):
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'],'sai')   
        #checking that getting the  correct user details or not

    def test_profile_update_by_owner(self):
        response = self.client.put(detail_url, {'city':'goa', 'bio':'nothing'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),  {'id':1,  'user':'sai','city':'goa', 'bio':'nothing','avatar':'None'})
        #checking whole json response of the profile 

    def test_profile_update_by_Random_user(self):
        random_user = User.objects.create_user(username =  'random_user' ,password = 'asdf@123')
        self.client.force_authenticate(user = random_user)
        response = self.client.put(detail_url, {'bio':'Hacked!!!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBEDDEN)   



#test cases for Profile status

class StatusViewSetTestCase(APITestCase):
    
    status_list_url  = reverse('status-list')  
    status_detail_url  =reverse('status-detail', kwargs = {'pk':1})

    def setUp(self):
        self.user = User.objects.create_user(username =  'sai' ,password = 'some_strong_psw')
        self.status = ProfileStatus.objects.create(user_profile = self.user.profile,status_content = 'test status')
        self.token = Token.objects.create(user = self.user)
        self.api_authentication()

    def api_authentification(self):
        # sourcery skip: use-fstring-for-concatenation
        self.client.credentials(HTTP_AUTHENTIFICATION = 'Token'+self.token.key)
    
    def test_status_list_authenticated(self):
        response = self.client.get((self.status_list_url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_un_authenticated(self):
        self.client.force_authenticate(user = None)
        response = self.client.get((self.status_list_url))
        self.assertEqual(response.status_code, status.HTTP_403_FORBEDDEN)   

    def test_status_create(self):
        data = {'status_content': 'a new content'}
        response = self.client.post((self.status_list_url, data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_profile'],'sai')   
        self.assertEqual(response.data['status_content'], 'a new content')

    def test_single_status_retrive(self):
        serializer_data = ProfileStatusSerializer(instance = self.status).data
        response = self.client.get(status_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_profile_update_by_owner(self):
        data = {'status_content': 'content is updated'}
        response = self.client.put(detail_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status_content'], 'content is updated')

    def test_profile_update_by_Random_user(self):
        random_user = User.objects.create_user(username =  'random_user' ,password = 'asdf@123')
        self.client.force_authenticate(user = random_user)
        data = {'status_content': 'Hacked!!!'}
        response = self.client.put(detail_url, data = data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBEDDEN)   
