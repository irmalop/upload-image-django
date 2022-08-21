from email.policy import default
from tabnanny import verbose
from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from cloudinary.models import CloudinaryField

def upload_load(instance, filename):
    return f'photos_users/{instance.email}/{filename}'


# Create your models here.

class  UserManager(BaseUserManager):
    def create_user(self, email, passsword=None, **extra_fields):
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(passsword)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, passsword=None, **extra_fields):
        user = self.model(
            email = self.normalize_email(email),
            is_active = True, 
            is_superuser = True,
            is_staff = True,
            **extra_fields,
        )
        user.set_password(passsword)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=150, null = False, verbose_name='name',)
    email = models.EmailField(unique=True, max_length=100, null=False, verbose_name='email',)
    # phone = models.CharField(verbose_name='phone', max_length=10)
    image = CloudinaryField('image', null=True, default = "https://res.cloudinary.com/dsxskoosl/image/upload/v1661100873/media/photos_users/default_wx8z7u.jpg")
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    status_delete = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'user'
        ordering = ('id',)
    
    def __str__(self):
        return f'{self.name} {self.email}'