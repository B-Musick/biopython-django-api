from django.db import models
from django.contrib.auth.models import User

class SequenceFeatureLocation(models.Model):
    ref = models.TextField()
    ref_db = models.TextField()
    strand = models.TextField() 

class SequenceFeature(models.Model):
    # http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec%3Aseq_features
    feature_id = models.AutoField(primary_key=True)
    type = models.TextField()
    location = models.ForeignKey(SequenceFeatureLocation, on_delete=models.CASCADE)
    qualifiers = models.JSONField()
    
class SequenceRecord(models.Model):
    id = models.TextField(primary_key=True)
    seq = models.TextField()
    name = models.TextField()
    description = models.TextField()
    dbxrefs = models.JSONField()
    features = models.ForeignKey(SequenceFeature, on_delete=models.CASCADE)
    annotations = models.JSONField()
    letter_annotations = models.JSONField()
    # On delete - if delete user, then should delete all of the sequence_records it has
    # can access all sequenceRecords through '.sequence_records'
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sequence_records")
