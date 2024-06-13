from django.shortcuts import render
from Bio import SeqIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from io import StringIO
from file_upload_api.serializer import FastaFileSerializer

def removeID(record):
    # Need to delete id since it wase causing errors
    record.biopython_id = record.id
    del record.id
    return record

# Create your views here.
@api_view(['POST'])
def upload(request):
    # Receive fasta or genbank file (check the type)
    f = StringIO(request.FILES['file'].read().decode("utf-8"))
    
    serializer = FastaFileSerializer({"records":map(removeID,SeqIO.parse(f, request.POST['fileType']))})
    print(serializer.data)
    return Response(serializer.data)

def help(request):
    return help(SeqIO)
