from django.contrib import admin

from api.models import Item

# Регистрируем модель в админке
admin.site.register(Item)
