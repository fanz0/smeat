from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from smapp.utils import sendTransaction
from django.shortcuts import get_object_or_404
import hashlib

def random_number():
    return User.objects.make_random_password(length=10,allowed_chars='123456789')

# Create your models here.
class Lot(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    tracking_code=models.CharField(max_length=10,default=random_number)
    hash=models.CharField(max_length=64,default=None,blank=True)
    txId=models.CharField(max_length=66,default=None,blank=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.text.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

    def publish(self):
        self.save()

    def __str__(self):
        if not self.hash:
            return str(self.writeOnChain())
        else:
            return self.title

class ip(models.Model):
    pub_date=models.DateTimeField('date published')
    ip_address=models.GenericIPAddressField()