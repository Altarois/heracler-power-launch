
from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from uuid import uuid4
from client.models import client

#generate token

def generateUUID():
    return str(uuid4())

# Create your models here.

class coach(models.Model):

    name = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='images/',null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact your coach')
    salle = models.ManyToManyField('salle', blank=True)

    def __str__(self):
       return self.name

class salle(models.Model):

    name = models.CharField(max_length=45, unique=True)
    description = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = PhoneField(blank=True, help_text='Contacte ta salle de sport')
    picture = models.ImageField(upload_to='images/',null=True, blank=True)
    map = models.CharField(max_length=555)

    def __str__(self):
       return self.name

    #def __str__(self):
    #   return self.name

    

class session(models.Model):
    name = models.CharField(max_length=80)
    clients = models.ManyToManyField(client, blank=True, related_name="sessions")
    coach = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length=256)
    timing = models.DateTimeField(null=True, blank=True)
    estimation = models.IntegerField(null=True , blank=True)


    def __str__(self):
       return self.name


class category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
       return self.name

class difficulty(models.Model):
    level = models.CharField(max_length=45)

    def __str__(self):
       return self.level


class exercise(models.Model):

    name = models.CharField(max_length=80)
    picture = models.ImageField(upload_to='images/',null=True, blank=True)
    session = models.ManyToManyField(session, null=True, blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True)
    difficulty = models.ForeignKey(difficulty, on_delete=models.CASCADE, null=True)


    def __str__(self):
       return self.name





class task(models.Model):

    REST_CHOICES = (
        (1, '15 seconds'),
        (2, '30 seconds'),
        (3, '1 minute'),
        (4, '1 minute 30 sec'),
        (5, '2 minutes')
    )

    SET_CHOICES = (
        (1, 'ONE'),
        (2, 'TWO'),
        (3, 'THREE'),
        (4, 'FOUR'),
        (5, 'FIVE')
    )

    reference = models.ForeignKey(exercise, on_delete=models.CASCADE , null=True, blank=True)
    session = models.ForeignKey(session, on_delete=models.CASCADE , null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=300, null=True)
    set = models.IntegerField(choices=SET_CHOICES, default=0)
    rest_time = models.IntegerField(choices=REST_CHOICES, default=0)

    def __str__(self):
       return self.name

class code(models.Model):


    token = models.CharField(max_length=80, unique=True, default=generateUUID())



    def __str__(self):
       return self.token
        #self.reference.username
















