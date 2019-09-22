from django.db import models

class LoverData(models.Model):
    boyfrnd_name=models.CharField(max_length=20)
    girlfrnd_name=models.CharField(max_length=30)
