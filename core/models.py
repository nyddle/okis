from django.db import models


OKIS_THEMES = {
    'auto' : u'Автомобили',
    'business' : u'Бизнес',
    'computers' : u'Компьютеры',
    'sport' : u'Спорт'
}

class OkisTemplate(models.Model):
    name = models.CharField(max_length=200)
    html = models.CharField(max_length=200)
    css  = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)

class OkisSite(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

