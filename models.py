from django.db import models
from .db_connect import db

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

test_collection = db['test']