from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
# Create your models here.

#* Eğer Kullandığımız User tablosu bize yetmez ise ilave yöntemler kullanabiliriz;
#? 1
# User modeli --> class User(AbstractUser): inherit edilerek yapılmış
# Biz de AbstractUser'dan  inherit ederek kendi User modelimizi oluşturabiliriz.
# Buna exdending user table deniyor,

# class MyUser(AbstractUser):
#   pass

# base.py içine;
# AUTH_USER_MODEL = "users.MyUser" --> ekle

#? 2
# yeni bir tablo oluşturup, bunu onetoone ile mevcut User tablosuna bağlayarak yapma;
# böylece mevcut User'lara ilave fieldlar ekleyebiliriz.
# Şimdi bu yöntemi kullanıp her bir User'ın Profile bilgilerini tutacağımız bir Profile Tablosu eklicez,

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  display_name = models.CharField(max_length=30, blank=True, null=True)
  avatar = models.ImageField(upload_to="pictures", default="avatar.png")
  # projelerde static'ler db olmaz, başka bir depolama alanında olur
  # https://django-storages.readthedocs.io/en/latest/
  
  bio = models.TextField(blank=True, null=True)
  
  def __str__(self):
    return f"{self.user.username}'s Profile"
      
  
  