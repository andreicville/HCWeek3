
from django.test import TestCase, Client
from django.urls import reverse
from deploy_app import views
from urllib.parse import urlencode
from models import Bikes, Brand, Parts, Accesories
from django.core.management import call_command

class test_user(TestCase):

    # Load test data from database fixture.
    def setUp(self):
        call_command('loaddata', 'fixture.json', verbosity = 0)

    # Unit test. Verify that bike with id 1 already exists. (This bike is in our fixture data.)
    def test_verify_bike_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    # Test API endpoint that will create a new bike, not in our fixture data.
    def test_new_bike(self):
        data = {
                "brand": "Trek",
                "nodel": "750",
                "category": "Hybrid",
                "frame_size": "8",
                "used": "False",
               }

        response_post = self.client.post('/api/v1/bikes/create/', data)
        response = self.client.get('/api/v1/bikes/1/')
        self.assertContains(response_post, 'true')
        self.assertContains(response, 'true')

   
    def tearDown(self):
        pass