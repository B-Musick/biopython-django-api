from django.test import TestCase
from rest_framework import status
from django.urls import reverse;
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Reverse takes in view name and gives us the path to the rout
from biopython_api.tests import GlobalTestCase

class ProteinApiTests(GlobalTestCase):
    def setUp(self):
        # user = User.objects.get(id=1)
        # user = User.objects.create_user(username='brendy', email='bmuze1@gmail.com', password='test')
        # client = APIClient()
        # refresh = RefreshToken.for_user(user)
        # self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        super(ProteinApiTests, self).setUp()

        self.uniprot_url = reverse('uniprot')
        self.protein_url = reverse('protein')
        
        # return super().setUp()
    
    def tearDown(self):
        # Run after done
        return super(ProteinApiTests, self).tearDown()
    
    def test_uniprot_response(self):
        response = self.client.get(
            self.uniprot_url, 
            {
                "accessions": "B5ZC00,A2Z669"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual("SYG_UREU1",response.data[0]['entry_name'])
        self.assertEqual(
            "MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK"
            ,response.data[0]['sequence']
        )


        self.assertEqual("CSPLT_ORYSI",response.data[1]['entry_name'])
        self.assertEqual(
            "MRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAPGTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYALLVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATAMAFISWFALAPSCVLNFWSMASR"
            ,response.data[1]['sequence']
        )

    def test_protein_submission(self):
        protein = {
            "entry_name": "CSPLT_ORYSI",
            "sequence": "MRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAPGTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYALLVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATAMAFISWFALAPSCVLNFWSMASR"
        }

        response = self.client.post(
            self.protein_url, protein, format="json"
        )
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data["entry_name"], "CSPLT_ORYSI")
        self.assertEqual(response.data["sequence"], "MRASRPVVHPVEAPPPAALAVAAAAVAVEAGVGAGGGAAAHGGENAQPRGVRMKDPPGAPGTPGGLGLRLVQAFFAAAALAVMASTDDFPSVSAFCYLVAAAILQCLWSLSLAVVDIYALLVKRSLRNPQAVCIFTIGDGITGTLTLGAACASAGITVLIGNDLNICANNHCASFETATAMAFISWFALAPSCVLNFWSMASR")