from django.db import models


class CatagoryManager(models.Manager):
    def available(self, *args, **kwargs):
        return self.filter(available=True)
