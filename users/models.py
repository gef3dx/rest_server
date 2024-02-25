from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    phone = models.CharField(verbose_name='Телефон', max_length=255)
    email = models.EmailField(verbose_name='Email', unique=True,
                              max_length=255)

    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_staff = models.BooleanField(verbose_name='Есть доступ в админку',
                                   default=False)
    is_superuser = models.BooleanField(verbose_name='Супер пользватель',
                                       default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

# Method POST
# {
#     "first_name": "John",
#     "last_name": "Smith",
#     "phone": "9604018811",
#     "email": "john@mail.ru",
#     "password": "German528872",
#     "re_password": "German528872"
# }
