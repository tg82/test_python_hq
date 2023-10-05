from django.contrib import admin

from .models import Product, Lesson, MyUser



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	"""
	Класс для предоставления продукта.
	"""
	list_display = ('pk', 'title', 'owner')
	list_display_links = ('pk',)
	ordering = ('pk',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	"""
	Класс для предоставления урока.
	"""
	list_display = ('pk', 'name', 'link', 'viewing', 'products')
	list_display_links = ('pk',)
	ordering = ('pk',)

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
	"""
	Класс для предоставления пользователя.
	"""
	list_display = ('pk', 'fullName', 'email', 'user', 'lesson', 'timeView', 'checkView')
	list_display_links = ('pk',)
	ordering = ('pk',)