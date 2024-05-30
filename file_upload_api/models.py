from django.db import models
from entrez_api.models import SequenceRecord

# Create your models here.
class FastaFile(models.Model):
    id = models.AutoField(primary_key=True)
    records = models.ForeignKey(SequenceRecord, on_delete=models.CASCADE)

    