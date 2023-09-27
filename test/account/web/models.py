from django.db import models


# Create your models here.
class Model(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default=True)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.name
