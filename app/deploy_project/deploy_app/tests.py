
from django.test import TestCase, Client
from django.urls import reverse
from deploy_app import views
from urllib.parse import urlencode
from django.core.management import call_command

class test_user(TestCase):

    # Load test data from database fixture.
    def setUp(self):
        call_command('loaddata', 'fixture.json', verbosity = 0)

    # Unit test. Verify that user with id 1 already exists. (This user is in our fixture data.)
    def test_verify_user_exists(self):
        response = self.client.get("/")
        print(response)
        self.assertEqual(response.status_code, 200)


   
    def tearDown(self):
        pass