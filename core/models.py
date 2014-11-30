from django.db import models
#from django.contrib.auth.models import User

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
    #TODO connect with Account or django User
    #owner = models.ForeignKey(User)
    template = models.ForeignKey(OkisTemplate)
    owner_email = models.CharField(max_length=200)


