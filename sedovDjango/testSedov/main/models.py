from django.db import models

# Create your models here.


class Products(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	image = models.CharField(max_length=255)

	class Meta:
		verbose_name_plural = "Products"