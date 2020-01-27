from django.db import models

# Create your models here.
class Pizza(models.Model):
    terkibi=models.CharField(max_length=50)
    hara=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=50)
    tarix=models.DateField(auto_now=True)
    qeyd=models.TextField(unique=True)
    olcu=models.ForeignKey('Olcu',on_delete=models.CASCADE)

class Olcu(models.Model):
    BALACA ='BALACA'
    ORTA = 'ORTA'
    BOYUK='BOYUK'

    PIZZA_OLCULERI=[
        (BALACA,'Balaca'),
        (ORTA,'Orta'),
        (BOYUK,'Boyuk'),
    ]

    title=models.CharField(max_length=10,choices=PIZZA_OLCULERI,default=BOYUK,)
    def __str__(self):
        return self.title


