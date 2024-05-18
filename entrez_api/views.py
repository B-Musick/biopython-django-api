from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Bio import Entrez
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
# Views responsible for returning our data

'''
Will need to use ESearch to search term and getrecords by their ids
- Then use the Efetch with the id to get the value

https://biopython.org/DIST/docs/tutorial/Tutorial.html#sec197
'''
@api_view(['GET'])
def dbs_list(request):
    Entrez.email = "bmuze1@gmail.com"
    stream = Entrez.einfo()
    record = Entrez.read(stream)
    return Response(record['DbList'])

@api_view(['POST'])
def search(request):
    Entrez.email = "bmuze1@gmail.com"
    stream = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
    record = SeqIO.read(stream, "genbank") # Seq object, can treat like string - See chapter 3 - https://biopython.org/DIST/docs/tutorial/Tutorial.html#sec17
    stream.close()
    # print(str(record.seq))
    return Response({'description':record.description, 'sequence': str(record.seq)})

# def getIds(searchTerm):

