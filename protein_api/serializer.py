from protein_api.models import SwissProtRecord
from rest_framework import serializers

class SwissProtRecordSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SwissProtRecord
        fields = ["entry_name", "sequence"]
        # extra_kwargs = {"author": {"read_only": True}} # Dont want someone to set who author is, it is automatically set