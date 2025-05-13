from django.db import models

# Create your models here.

class Categories(models.Model):
	name = models.CharField('Название категории', max_length=250)
	description = models.TextField('Описание', max_length=250)

	def __str__(self):
		return self.name

class User(models.Model):
	login = models.CharField('Логин', max_length=50) 
	password = models.CharField('Пароль', max_length=50)
	email = models.CharField('Почта', max_length=50)
	phone = models.CharField('Телефон', max_length=12)
	address = models.CharField('Адрес', max_length=100)




class Manufacturers(models.Model):
	name = models.CharField('Название компании', max_length=250)
	country = models.CharField('Страна', max_length=250)
	contact_info = models.CharField('Информация', max_length=250)
	def __str__(self):
		return self.name


class Products(models.Model):
	name = models.CharField('Название товара', max_length=250)

	category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)



	description = models.CharField('Описание товара', max_length=250)
	price =	models.DecimalField('Цена', max_digits=8, decimal_places=2)
	stock_quantity = models.IntegerField('Количество на складе')
	image = models.CharField('Картинка', max_length=250, default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'