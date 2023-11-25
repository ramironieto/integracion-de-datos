from django.db import models
class Property(models.Model):
    BARRIOS_CHOICES = [
        ('aguada', 'Aguada'),
        ('atahualpa', 'Atahualpa'),
        ('barrio sur', 'Barrio Sur'),
        ('bella vista', 'Bella Vista'),
        ('buceo', 'Buceo'),
        ('capurro', 'Capurro'),
        ('centro', 'Centro'),
        ('carrasco', 'Carrasco'),
        ('carrasco norte', 'Carrasco Norte'),
        ('carrasco sur', 'Carrasco Sur'),
        ('cerrito', 'Cerrito'),
        ('cerro', 'Cerro'),
        ('cordón', 'Cordón'),
        ('jacinto vera', 'Jacinto Vera'),
        ('la blanqueada', 'La Blanqueada'),
        ('la comercial', 'La Comercial'),
        ('la figurita', 'La Figurita'),
        ('la teja', 'La Teja'),
        ('larrañaga', 'Larrañaga'),
        ('malvín', 'Malvín'),
        ('malvín norte', 'Malvín Norte'),
        ('malvín nuevo', 'Malvín Nuevo'),
        ('maroñas', 'Maroñas'),
        ('mercado modelo', 'Mercado Modelo'),
        ('palermo', 'Palermo'),
        ('parque batlle', 'Parque Batlle'),
        ('parque rodó', 'Parque Rodó'),
        ('paso de las duranas', 'Paso de las Duranas'),
        ('paso molino', 'Paso Molino'),
        ('piedras blancas', 'Piedras Blancas'),
        ('pocitos', 'Pocitos'),
        ('pocitos nuevo', 'Pocitos Nuevo'),
        ('prado', 'Prado'),
        ('punta carretas', 'Punta Carretas'),
        ('reducto', 'Reducto'),
        ('sayago', 'Sayago'),
        ('tres cruces', 'Tres Cruces'),
        ('tres ombúes', 'Tres Ombúes'),
        ('unión', 'Unión'),
        ('villa del cerro', 'Villa del Cerro'),
        ('villa española', 'Villa Española'),
        ('villa garcía', 'Villa García'),
        ('villa muñoz', 'Villa Muñoz'),
    ]

    TIPO_CHOICES = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
        ('otros', 'Otros'),
    ]

    titulo = models.CharField(max_length=60)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, null=True)
    cuartos = models.PositiveSmallIntegerField(null=True)
    metros_cuadrados = models.PositiveIntegerField(null=True)
    barrio = models.CharField(max_length=50, choices=BARRIOS_CHOICES, null=True)
    precio = models.PositiveIntegerField(null=True)
    gastos_comunes = models.PositiveIntegerField(null=True)
    direccion = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

