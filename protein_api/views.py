from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from Bio import ExPASy
from Bio import SwissProt
from protein_api.serializer import SwissProtRecordSerializer
from protein_api.models import SwissProtRecord
# Create your views here.
@api_view(['GET'])
def uniprot(request):
    # From the request it will take term from the search bar and use it for the term
    accessions = request.query_params['accessions']
    accessions_array = accessions.split(',')
    records = []

    for accession in accessions_array:
    # id_list = retrieveIdsFromEntrez(db_type, search_term, max_results)
        handle = ExPASy.get_sprot_raw(accession)
        record = SwissProt.read(handle)
        records.append(record)
        handle.close()

    # records = fetchSeqRecordsFromId("nucleotide", id_list, "gb")

    serializer = SwissProtRecordSerializer(records, many=True)
    return Response(serializer.data)

class SwissProtRecordListCreate(generics.ListCreateAPIView):
    serializer_class = SwissProtRecordSerializer # Data passed will tell us if valid
    permission_classes = [IsAuthenticated] # Cant call route unless authenticated and pass JWT token

    def get_queryset(self):
        user = self.request.user # Get authenticated user, and use to filter records written by user
        return SwissProtRecord.objects.filter(author=user)
    
    def perform_create(self, serializer):
        # Pass serializer and validate, then add any extras that need to manually do
        if(serializer.is_valid()):
            serializer.save(author=self.request.user)
        else: 
            print(serilizer.errors)