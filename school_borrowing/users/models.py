# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, nama, role, password=None, kelas=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, nama=nama, role=role, kelas=kelas)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, email, nama, password=None):
        return self.create_user(email, nama, 'Admin', password)

    def create_student(self, email, nama, password=None, kelas=None):
        return self.create_user(email, nama, 'Siswa', password, kelas)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Siswa', 'Siswa'),
    )
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    kelas = models.CharField(max_length=20, null=True, blank=True)  # Hanya untuk siswa

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama', 'role']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
