from django.db import models

class Role (models.Model):
    Id=models.IntegerField(max_length=300,primary_key= True) 	            #The unique id to identify the role.
    Title=models.CharField(max_length=75,null=False) 	                    #The role title.
    Slug=models.CharField(max_length=100,null=False) 	                    #The unique slug to search the role.
    Description=models.CharField(null=True) 	                            #The description to mention the role.
    Type=models.SmallIntegerField(null=False,default=0) 	                #The role type to distinguish among system and organization roles.
    Active=models.SmallIntegerField(null=False,default=0) 	                #The flag to check whether the role is currently active.
    Created=models.DateTimeField(null=False)                                #At 	It stores the date and time at which the role is created.
    Updated=models.DateTimeField(null=False)                                #At 	It stores the date and time at which the role is updated.
    Content=models.CharField(max_length=300,null=False)                     #The complete details about the role.