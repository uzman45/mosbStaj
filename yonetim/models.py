from django.db import models

# Create your models here.
class User(models.Model):
  adi=models.CharField(max_length=50)
  soyadi=models.CharField(max_length=50)
  telNo=models.CharField(max_length=11)
  eMail=models.EmailField(max_length=60)
  def __str__(self):
  	return self.adi+" "+self.soyadi
