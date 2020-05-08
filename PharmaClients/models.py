from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class DrugList(models.Model):
    Drug_name = models.CharField(max_length=255)
    Drug_Expiry = models.DateTimeField()
    Added_By = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Drug_Manufacturer = models.CharField(max_length = 255)
    Preview = models.ImageField()
    Drug_type = models.CharField(max_length=255)

    def __str__(self):
        return self.Drug_name

