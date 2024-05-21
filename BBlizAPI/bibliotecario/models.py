from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator

class BibliotecarioUserManager(BaseUserManager):
    def create_user(self, usuario, email, password=None, **extra_fields):
        if not usuario:
            raise ValueError('Debes ingresar el usuario')
        if not email:
            raise ValueError('Debes ingresar el correo')
        email = self.normalize_email(email)
        user = self.model(usuario=usuario, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(usuario, email, password, **extra_fields)

class Bibliotecario(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    usuario = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text=(
            "Requerido. 150 caracteres o menos. Letras, dígitos y @/./+/-/_ únicamente."
        ),
        validators=[username_validator],
        error_messages={
            "unique": ("Ya existe un usuario con ese nombre."),
        },
    )
    nombres = models.CharField(max_length=150, blank=True)
    apellido_paterno = models.CharField(max_length=150, blank=True)
    apellido_materno = models.CharField(max_length=150, blank=True)
    direccion = models.CharField(max_length=150, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    email = models.EmailField("email address", blank=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text=("Designa si el usuario puede iniciar sesión en este sitio de administración."),
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=("Designa si este usuario debe ser tratado como activo. Desmarcar esto en lugar de eliminar cuentas"),
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = BibliotecarioUserManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.usuario