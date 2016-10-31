from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(
            self,
            email,
            last_name,
            first_name,
            nickname,
            phone_number,
            password=None
    ):
        user = self.model(
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self,
            email,
            last_name,
            first_name,
            nickname,
            phone_number,
            password=None
    ):
        user = self.model(
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
            phone_number=phone_number,
        )

        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('last_name', 'first_name', 'nickname', 'phone_number')

    objects = MyUserManager()

    def get_full_name(self):
        return '%s%s' % (self.last_name, self.first_name)

    def get_short_name(self):
        return self.first_name

    # 폰번호 '-' 문자 예외처리
    def save(self, *args, **kwargs):
        if '-' in self.phone_number:
            self.phone_number = self.phone_number.replace('-', '')
        super().save(*args, **kwargs)