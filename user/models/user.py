from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from ..managers import UserManager
from .user_role import UserRole


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = None
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    last_name = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    age = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    role = models.CharField(max_length=1, choices=UserRole.choices, default=UserRole.default)
    last_seen = models.DateTimeField(default=timezone.now)

    is_first_name_private = models.BooleanField(default=False)
    is_age_private = models.BooleanField(default=True)
    is_email_private = models.BooleanField(default=True)
    is_date_joined_private = models.BooleanField(default=True)

    @property
    def user_info_first_name(self):
        if self.is_first_name_private:
            return None
        return self.first_name

    @property
    def user_info_age(self):
        if self.is_age_private:
            return None
        return self.age

    @property
    def user_info_email(self):
        if self.is_email_private:
            return None
        return self.email

    @property
    def user_info_date_joined(self):
        if self.is_date_joined_private:
            return None
        return self.date_joined

    @property
    def user_info_preferences(self):
        return [_.preference.code for _ in self.preferences.all()]

    @property
    def user_info_targets(self):
        return [_.target.code for _ in self.targets.all()]

    @property
    def access_token(self):
        from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

        return TokenObtainPairSerializer(self).get_token(self).access_token
