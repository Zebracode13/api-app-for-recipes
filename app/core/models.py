from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionMixin)

# Create your models here.
class UserManger(BaseUserManager):

    def create_user(self, email, password=None, **extra_feilds):
        """Creates and saves a new user"""
        user = self.model(email=email, **extra_feilds)
        user.set_password(password)
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionMixin):
    """costum user modle that supporst wmail instead of username"""
    email = models.EmailField(max_length=264, unique=True)
    name = models.CharField(max_length=264)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManger()
    USERNAME_FIELD = 'email'

