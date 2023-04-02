from django.db import models

# Create your models here.
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class User(AbstractBaseUser, BaseUserManager):
    HigherEducation, PLACED, OTHER = 1, 2, 3
    STATUS_CHOICES = (
        (HigherEducation, "highereducation"),
        (PLACED, "placed"),
        (OTHER, "Other")
    )

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_regex = RegexValidator(regex=r'^([1-9][0-9]{9})$', message='only numbers are allowed')
    # Validators should be a list
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    roll_no = models.CharField(max_length=100, unique=True, null=False)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=True, blank=True)
    firm = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(null=False, blank=False)
    image = models.ImageField(upload_to="alumnipage/images/")

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_name(self):
        return self.get_full_name()

    def is_admin(self):
        return self.is_staff

    def is_super_admin(self):
        return self.is_superuser

    '''def save(self, *args, **kwargs):
        if self.date_of_birth and self.date_of_birth > datetime.date.today():
            raise ValidationError("date in future")
        super(User, self).save(*args, **kwargs)'''