from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Bio import ExPASy
from Bio import SwissProt
from protein_api.serializer import SwissProtRecordSerializer

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