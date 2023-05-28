from django.core.validators import MinValueValidator
from django.db import models
from user.models import User
from levels.models import Config


class UserLevel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='level')
    current_level = models.ForeignKey(Config, on_delete=models.SET_NULL, null=True)

    total_exp = models.FloatField(default=0, validators=[MinValueValidator(0)])

    def get_current_level(self):
        if not self.current_level:
            config = Config.objects.filter(exp__lte=self.total_exp).last()

            self.current_level = config
            self.save()

        return self.current_level

    def process_level(self):
        if not self.current_level or self.current_level.exp <= self.total_exp:
            self.get_current_level()
