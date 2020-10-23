from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)

# Create your models here.
class UserManger(BaseUserManager):
    def create_user(self, email, password=None, **extra_feilds):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('User must enter an email!!')
        user = self.model(email=self.normalize_email(email), **extra_feilds)
        user.set_password(password)
        user.save(using=self.db)

        return user


    def create_superuser(self, email, password):
        """Creates and saves a supper user"""
        user = self.create_user(email, password)
        user.is_supperuser = True
        user.save(using=self.db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    """costum user modle that supporst wmail instead of username"""
    email = models.EmailField(max_length=264, unique=True)
    name = models.CharField(max_length=264)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManger()
    USERNAME_FIELD = 'email'