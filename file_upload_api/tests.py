from django.test import TestCase
from rest_framework import status
from django.urls import reverse;
from rest_framework.test import APITestCase, APIClient
import os
from biopython_api.tests import GlobalTestCase

module_dir = os.path.dirname(__file__)  # get current directory

class EntrezTests(GlobalTestCase):
    def setUp(self):
        super(GlobalTestCase, self).setUp()
        self.upload_url = reverse('upload')

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

    def test_upload_fasta_response(self):
        file_path = os.path.join(module_dir, "public/sequence.fasta")

        response = ''

        with open(file_path) as file:
            response = self.client.post(self.upload_url, {"fileType":"fasta", "file":file})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data)[0], 'records')
        self.assertEqual(len(response.data), 1)
        
        record = response.data["records"][0]

        self.assertIn("biopython_id", record)
        self.assertIn("features", record)
        self.assertIn("annotations", record)
        self.assertIn("seq", record)
        self.assertIn("name", record)
        self.assertIn("description", record)
        self.assertIn("dbxrefs", record)
        self.assertIn("letter_annotations", record)

        self.assertEqual("NM_005546.3", record["biopython_id"])

    def test_upload_genbank_response(self):
        file_path = os.path.join(module_dir, "public/sequence.gb")

        response = ''

        with open(file_path) as file:
            response = self.client.post(self.upload_url, {"fileType":"gb", "file":file})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data)[0], 'records')
        self.assertEqual(len(response.data), 1)
        
        record = response.data["records"][0]

        self.assertIn("biopython_id", record)
        self.assertIn("features", record)
        self.assertIn("annotations", record)
        self.assertIn("seq", record)
        self.assertIn("name", record)
        self.assertIn("description", record)
        self.assertIn("dbxrefs", record)
        self.assertIn("letter_annotations", record)

        self.assertEqual("AY530803.2", record["biopython_id"])