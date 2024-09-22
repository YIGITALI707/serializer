from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    photo=models.ImageField(upload_to='rasm')


    def __str__(self):
        return self.title


class Products(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    created_add=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cats(models.Model):
    ism=models.CharField(max_length=150)
    turi=models.CharField(max_length=20)
    rangi=models.CharField(max_length=20)
    xususiyati=models.TextField()

    def __str__(self):
        return self.ism
