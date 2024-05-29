from rest_framework import serializers
from entrez_api.models import SequenceRecord
from entrez_api.models import SequenceFeature
from entrez_api.models import SequenceFeatureLocation
import json

class SequenceFeatureLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SequenceFeatureLocation
        fields = "__all__"

class SequenceFeatureSerializer(serializers.ModelSerializer):
    location = SequenceFeatureLocationSerializer()
    
    class Meta:
        model = SequenceFeature
        fields = "__all__"

class SequenceRecordSerializer(serializers.ModelSerializer):
    features = SequenceFeatureSerializer(many=True)
    annotations = serializers.DictField(child=serializers.CharField())

    class Meta:
        model = SequenceRecord
        fields = "__all__"