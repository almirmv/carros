# precisa avisar dentro de apps.py do app car para ativar o signals
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_bio
def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
        )['total_value']
    # agregate ia retornar dicionario {'total_value': 15656.00}
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )


# esse decorator fica escutando por "pre_save" da tabela "Car" !
# quando detecta uma, ele executa a função abaixo dele
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    '''Signal de Carro novo cria novo inventario'''
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    '''Signal de Carro novo cria novo inventario'''
    car_inventory_update()

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    # se nao tiver foto...colocar uma padrao
    if not instance.photo:
        instance.photo = 'cars/velocipede.jpg'

    # Se carro nao vier bio, cria uma com IA
    if not instance.bio:
        try:
            ai_bio = get_car_ai_bio(
                instance.brand,
                instance.model,
                instance.model_year
                )
            instance.bio = ai_bio
        except Exception as e:
            print(f'[OPEN_AI ERROR]: {e}')
