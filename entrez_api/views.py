from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Bio import Entrez
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import json
from entrez_api.serializer import SequenceRecordSerializer

'''
Will need to use ESearch to search term and getrecords by their ids
- Then use the Efetch with the id to get the value

https://biopython.org/DIST/docs/tutorial/Tutorial.html#sec197
'''
def removeID(record):
    # Need to delete id since it wase causing errors
    record.biopython_id = record.id
    del record.id
    return record

@api_view(['GET'])
def dbs_list(request):
    Entrez.email = "bmuze1@gmail.com"
    stream = Entrez.einfo()
    record = Entrez.read(stream)
    return Response(record['DbList'])

@api_view(['GET'])
def search(request):
    Entrez.email = "bmuze1@gmail.com"
    # From the request it will take term from the search bar and use it for the term
    search_term = request.query_params['searchTerm']
    print(search_term)
    max_results = request.query_params['maxResults']
    db_type= request.query_params['databaseType']

    id_list = retrieveIdsFromEntrez(db_type, search_term, max_results)

    records = fetchSeqRecordsFromId("nucleotide", id_list, "gb")

    serializer = SequenceRecordSerializer(map(removeID, records), many=True)
    return Response(serializer.data)

def retrieveIdsFromEntrez(db_type, search_term, max_results):
    # Perform Entrez.esearch
    handle = Entrez.esearch(db=db_type, term=search_term, retmax=max_results)
    rec_list = Entrez.read(handle)
    handle.close()

    return rec_list['IdList']

def fetchSeqRecordsFromId(dbToSearch, ids, returnType):
    # Will get a list of records
    stream = Entrez.efetch(db=dbToSearch, id=ids, rettype=returnType)
    records = list(SeqIO.parse(stream, returnType)) # Seq object, can treat like string - See chapter 3 - https://biopython.org/DIST/docs/tutorial/Tutorial.html#sec17
    stream.close()
    
    return records
    