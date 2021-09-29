from django.db import models


class user (models.Model):

    id=models.IntegerField(max_length=20,primary_key=True),
    FristName = models.CharField(max_length=255, null=False),
    MiddleName = models.CharField(max_length=255, null=False),
    LastName = models.CharField(max_length=255, null=False),
    Mobile = models.CharField(max_length=15, null=False),
    Email = models.CharField(max_length=50, null=False),
    Password = models.CharField(max_length=255, null=False),
    registerAt = models.DateTimeField(null=False),
    LastLogin = models.DateTimeField(null=False),
    intro=models.CharField(max_length=150,),
    ProfileText=models.CharField(max_length=150,),
