from django.db import models

class Count(models.Model):
    date = models.DateField(auto_now_add=True)
