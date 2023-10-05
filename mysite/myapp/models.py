from django.contrib.auth.models import User
from django.db import models

"""
В этом задании у нас есть три бизнес-задачи на хранение:
Создать сущность продукта. 
У продукта должен быть владелец. 
Необходимо добавить сущность для сохранения доступов к продукту для пользователя.

Создать сущность урока.
Урок может находиться в нескольких продуктах одновременно. 
В уроке должна быть базовая информация: 
название,
ссылка на видео,
длительность просмотра (в секундах).

Урок могут просматривать множество пользователей. 
Необходимо для каждого фиксировать время просмотра и фиксировать статус “Просмотрено”/”Не просмотрено”. 
Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.

"""


class Product(models.Model):
	"""
	Модель продукта.
	"""
	title = models.CharField(max_length=128, blank=False, null=False, verbose_name='Название')
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
	                             related_name='owner', verbose_name='Владелец')


	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'
		ordering = ('pk',)

	def __str__(self):
		return self.title


class Lesson(models.Model):
	"""
	Модель урока.
	"""
	name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Название')
	link = models.CharField(max_length=128, blank=False, null=False, verbose_name='Ссылка на урок')
	viewing = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Длительность просмотра')
	products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='lessons', verbose_name='Продукт')

	class Meta:
		verbose_name = 'Урок'
		verbose_name_plural = 'Уроки'
		ordering = ('pk',)

	def __str__(self):
		return self.name


STATUS = [
	'Просмотрено',
	'Не просмотрено'
]

class MyUser(models.Model):
	'''
	Модель-класс. Содержит расширенную информацию о пользователе.
	'''
	fullName = models.CharField(max_length=64, default='Неизвестно', blank=False, verbose_name='Ф.И.О.')
	email = models.EmailField(max_length=64, default='Неизвестно', blank=False, verbose_name='Email-адрес')
	user: User = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, related_name='profile', verbose_name='Пользователь')
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=False, null=True, related_name='lesson', verbose_name='Урок')
	timeView = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Время просмотра', blank=False)
	checkView = models.BooleanField(verbose_name='Статус Просмотрено / Не просмотрено', blank=False)

	class Meta:
		verbose_name = 'Профиль пользователя'
		verbose_name_plural = 'Профили пользователей'
		ordering = ('pk',)