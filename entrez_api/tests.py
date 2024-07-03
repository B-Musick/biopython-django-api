from django.test import TestCase
from rest_framework import status
from django.urls import reverse;
from rest_framework.test import APITestCase, APIClient
from biopython_api.tests import GlobalTestCase
# Reverse takes in view name and gives us the path to the rout

# Create your tests here.
class EntrezTests(GlobalTestCase):
    def setUp(self):
        super(GlobalTestCase, self).setUp()
        # Run every time test is run
        self.dbs_list_url = reverse('dbs_list')
        self.search_url = reverse('search')

        return super().setUp()
    
    def tearDown(self):
        # Run after done
        return super(GlobalTestCase, self).tearDown()

    def test_dbs_list_response(self):
        response = self.client.get(self.dbs_list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 40)
        self.assertIn("nucleotide",response.data)
    
    def test_search_response(self):
        response = self.client.get(
            self.search_url, 
            {
                'databaseType': 'nucleotide', 
                'searchTerm':'CRT[Gene Name] AND "Plasmodium falciparum"[Organism]',
                'maxResults': 5
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual("PP842460.1",response.data[0]['biopython_id'])
