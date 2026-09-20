from django.db import models

# Create your models here.

class Teachers(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    image=models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return f'{self.name} - {self.subject} - {self.contact}'




class Students(models.Model):
    name=models.CharField(max_length=100)
    grade=models.CharField(max_length=50)
    section=models.CharField(max_length=15)
    contact=models.CharField(max_length=15)
    image=models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return f'{self.name} - {self.grade} - {self.section}'



