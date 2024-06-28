# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# import uuid

# class UUIDMixin(models.Model):
#     uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

#     class Meta:
#         abstract = True

# class StatusMixin(models.Model):
#     is_active = models.BooleanField(default=True)
#     is_deleted = models.BooleanField(default=False)

#     class Meta:
#         abstract = True

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, name, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, name, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, name, password, **extra_fields)

# class User(AbstractBaseUser, PermissionsMixin, UUIDMixin, StatusMixin):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
    
#     is_staff = models.BooleanField(default=False)

#     roles = models.ManyToManyField('Role', related_name='users')

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email

# class Permission(UUIDMixin):
#     name = models.CharField(max_length=255, unique=True)
#     code = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name

# class Role(UUIDMixin):
#     name = models.CharField(max_length=255, unique=True)
#     permissions = models.ManyToManyField(Permission, related_name='roles')

#     def __str__(self):
#         return self.name
