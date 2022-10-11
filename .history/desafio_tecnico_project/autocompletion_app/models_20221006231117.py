from django.db import models

# Create your models here.
class Words(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=200)

    class Meta: