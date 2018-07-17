from django.db import models
from django.urls import reverse

from .managers import manager
from core.models import BaseModel


class Catagory(BaseModel):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'catagory'
        verbose_name_plural = 'catagories'

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('shop:product_list_by_catagory', args=[self.slug])


class Product(BaseModel):
    catagory = models.ForeignKey(
        Catagory,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    objects = manager.ProductManager()

    class Meta:
        ordering = ('-created', )
        index_together = (
            ('id', 'slug'),
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('shop:product_detail', args=[str(self.pk), self.slug])
