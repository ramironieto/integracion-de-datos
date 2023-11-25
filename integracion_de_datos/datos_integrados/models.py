from django.db import models
class Property(models.Model):
    
    BARRIOS_CHOICES = [
    ('Aguada', 'Aguada'),
    ('Atahualpa', 'Atahualpa'),
    ('Barrio Sur', 'Barrio Sur'),
    ('Bella Vista', 'Bella Vista'),
    ('Buceo', 'Buceo'),
    ('Capurro', 'Capurro'),
    ('Carrasco', 'Carrasco'),
    ('Carrasco Norte', 'Carrasco Norte'),
    ('Carrasco Sur', 'Carrasco Sur'),
    ('Cerrito', 'Cerrito'),
    ('Cerro', 'Cerro'),
    ('Cordón', 'Cordón'),
    ('Jacinto Vera', 'Jacinto Vera'),
    ('La Blanqueada', 'La Blanqueada'),
    ('La Comercial', 'La Comercial'),
    ('La Figurita', 'La Figurita'),
    ('La Teja', 'La Teja'),
    ('Larrañaga', 'Larrañaga'),
    ('Malvín', 'Malvín'),
    ('Malvín Norte', 'Malvín Norte'),
    ('Malvín Nuevo', 'Malvín Nuevo'),
    ('Maroñas', 'Maroñas'),
    ('Mercado Modelo', 'Mercado Modelo'),
    ('Palermo', 'Palermo'),
    ('Parque Batlle', 'Parque Batlle'),
    ('Parque Rodó', 'Parque Rodó'),
    ('Paso de las Duranas', 'Paso de las Duranas'),
    ('Paso Molino', 'Paso Molino'),
    ('Piedras Blancas', 'Piedras Blancas'),
    ('Pocitos', 'Pocitos'),
    ('Pocitos Nuevo', 'Pocitos Nuevo'),
    ('Prado', 'Prado'),
    ('Punta Carretas', 'Punta Carretas'),
    ('Reducto', 'Reducto'),
    ('Sayago', 'Sayago'),
    ('Tres Cruces', 'Tres Cruces'),
    ('Tres Ombúes', 'Tres Ombúes'),
    ('Unión', 'Unión'),
    ('Villa del Cerro', 'Villa del Cerro'),
    ('Villa Española', 'Villa Española'),
    ('Villa García', 'Villa García'),
    ('Villa Muñoz', 'Villa Muñoz'),
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

