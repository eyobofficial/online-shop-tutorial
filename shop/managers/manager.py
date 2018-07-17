from django.db import models


class ProductManager(models.Manager):
    def available(self, *args, **kwargs):
        return self.filter(available=True)
