from rest_framework import serializers
from entrez_api.serializer import SequenceRecordSerializer
from file_upload_api.models import FastaFile

import json

class FastaFileSerializer(serializers.ModelSerializer):
    records = SequenceRecordSerializer(many=True)

    class Meta:
        model = FastaFile
        fields = "__all__"

# class SequenceFeatureSerializer(serializers.ModelSerializer):
#     location = SequenceFeatureLocationSerializer()
    
#     class Meta:
#         model = SequenceFeature
#         fields = "__all__"

# class SequenceRecordSerializer(serializers.ModelSerializer):
#     features = SequenceFeatureSerializer(many=True)
#     annotations = serializers.DictField(child=serializers.CharField())

#     class Meta:
#         model = SequenceRecord
#         fields = "__all__"