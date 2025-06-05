from django.db import models

# Create your models here.
class Bot(models.Model):
    interval_first = models.IntegerField()
    interval_second = models.IntegerField()
    key_word = models.TextField()
    ban_word = models.TextField()
    agent_promt = models.TextField()
    promt = models.TextField()
    proxy_host = models.CharField()
    proxy_port = models.CharField()
    proxy_user = models.CharField()
    proxy_password = models.CharField()