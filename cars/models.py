from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    # Função que exibe os objetos de forma legível nas interfaces administrativas
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    # models.PROTECT  => Gera um erro se alguém tentar deletar o pai que tem filhos relacionados.
    # models.CASCATE  => Deleta automaticamente todos os filhos relacionados quando o pai é deletado.
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') 
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    # Para campos de fotos (ImageField) obrigatório instalar a biblioteca Pillow (pip install pillow)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    # Função que exibe os objetos de forma legível nas interfaces administrativas
    def __str__(self):
        return self.model