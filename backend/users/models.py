from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

ACTIVE_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

class BaseModelMixin(models.Model):

    """
    Base model mixin. Date of create and date of update and soft-delete
    """

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    is_deleted = False

    class Meta:
        abstract = True



class User(AbstractUser, BaseModelMixin):

    address= models.CharField(max_length=150,blank=True,null=True)
    mobile_number= models.CharField(max_length=15,blank=True,null=True)
    aadhar_no = models.CharField(max_length=15,blank=True,null=True)
    active_status = models.CharField(blank=True, default='Active',max_length=8, choices=ACTIVE_CHOICES)

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    
    def __str__(self):
        return f"{self.pk},{self.username}"


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


