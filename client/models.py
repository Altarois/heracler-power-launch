from phone_field import PhoneField
from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
import uuid


def generateUUID():
    return str(uuid.uuid4().hex[:12].upper())








# Create your models here.
class client(models.Model):

    name = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=85)
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.URLField(null=True ,blank=True)
    affiliation = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client_coach")
    reference = models.OneToOneField(User, on_delete=models.CASCADE, null=True , blank=True)
    is_active = models.BooleanField(default=False)
    token = models.CharField(max_length=85)
    session_count = models.SmallIntegerField(default=0)


    def __str__(self):
       return self.name

    def getname(self):
        return self.coach.name

    def save(self, *args, **kwargs):
        self.token = generateUUID()
        super(client, self).save(*args, **kwargs)


class stats(models.Model):

    session_confirmed = models.ForeignKey('coach.session', on_delete=models.CASCADE,null=True, blank=True )
    link = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.comment