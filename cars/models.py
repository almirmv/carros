from django.db import models

class Brand(models.Model):
    name = models.CharField(verbose_name='Marca',max_length=200, unique=True)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    #id = models.AutoField(primary_key=True) # nao precisa django cria automatico
    model = models.CharField(verbose_name='Modelo',max_length=200)
    #brand = models.CharField(verbose_name="Marca",max_length=200)
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10,blank=True, null=True,verbose_name='placa')
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
        
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'