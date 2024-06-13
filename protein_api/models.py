from django.db import models

# Create your models here.
class SwissProtRecord(models.Model):
    sequence = models.TextField()
    entry_name = models.TextField()
    # description = models.TextField(blank=True)
    # dbxrefs = models.JSONField(null=True)
    # features = models.ForeignKey(SequenceFeature, on_delete=models.CASCADE, null=True)
    # annotations = models.JSONField(null=True)
    # letter_annotations = models.JSONField(null=True)
    # # On delete - if delete user, then should delete all of the sequence_records it has
    # # can access all sequenceRecords through '.sequence_records'
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sequence_records")
