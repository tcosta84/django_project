# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
#
#
# class UserManager(BaseUserManager):
#     def create_user(self, email,  password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
#
# class User(AbstractBaseUser):
#     # first_name = models.CharField(u'Primeiro nome', max_length=30)
#     # last_name = models.CharField(u'Último nome', max_length=30)
#     email = models.EmailField(
#         verbose_name=u'email address',
#         max_length=255,
#         unique=True,
#     )
#     # is_superuser = models.BooleanField(u'Superuser', default=False)
#     # is_active = models.BooleanField(default=True)
#     # is_admin = models.BooleanField(default=False)
#     # date_joined = models.DateTimeField(u'Data do cadastro', auto_now_add=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def get_full_name(self):
#         "Returns the first_name plus the last_name, with a space in between."
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()
#
#     def get_short_name(self):
#         return self.first_name
#
#     def __unicode__(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         return True
#
#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         return self.is_admin


class Customer(models.Model):
    user = models.OneToOneField(User)
    cpf = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
