from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class DrugList(models.Model):
    Drug_name = models.CharField(max_length=255)
    Drug_Expiry = models.DateTimeField()
    #Added_By = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Drug_Manufacturer = models.CharField(max_length = 255)
    Preview = models.ImageField()
    Drug_type = models.CharField(max_length=255)
    price = models.IntegerField(default=1)
    DateAdded = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Drug_name
    
class Delivery(models.Model):
    Country_Choice = (
    ('Ethiopia', "Ethiopia"),
    ('Kenya', 'Kenya'),
    ('Djbouti', 'Djbouti'),
    ('Somalia', 'Somalia'),
    ('Sudan',  'Sudan'),
    ('South Sudan', 'South Sudan'),
    ('Eritrea', 'Eritrea')
    )
    Country = models.CharField(choices=Country_Choice, max_length=30, null=False)
    City = models.CharField(max_length=100, null=False,)
    Street_Name = models.CharField(max_length=200, null=False,)
    House_No = models.IntegerField(null=False)
    
    
    def __str__(self):
        return str(self.Country) + " " + self.City + " " + self.Street_Name + " " + str(self.House_No)
   
class DrugOrder(models.Model):
    Drug_name = models.ForeignKey(DrugList, on_delete=models.CASCADE, related_name='Order')
    Order_Date = models.DateTimeField(auto_now=True)
    Ordered_By = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Order')
    Quantity = models.IntegerField(null=False)
    TotalPrice = models.IntegerField(null=False, default=1)
    Deliveries = models.OneToOneField(Delivery, on_delete=models.CASCADE, related_name='Deli')
    def __str__(self):
        return self.Ordered_By.username + " " + str(self.Order_Date) + " " + str(self.Drug_name.Drug_name)
    def get_absolute_url(self):
        return reverse('home')


    








    



