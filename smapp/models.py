from django.db import models
from django.utils import timezone
from django.conf import settings
import hashlib

# Create your models here.
class Lot(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    tracking_code=models.IntegerField()
    hash = models.CharField(max_length=32, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def publish(self):
        sel.save()

    def __str__(self):
        return self.title

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.text.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()