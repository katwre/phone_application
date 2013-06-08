from django.db import models

class Product(models.Model):
  key = models.CharField(max_length = 400,help_text="")
  value = models.TextField(max_length = 2000,help_text="")
  data_modyfikacji = models.DateTimeField(auto_now=True)
  czy_skasowane = models.BooleanField(default=False) #i wtedy np. nie dac uzytkownikowi praw do kasowania w profilu administracyjnym
  
  
 