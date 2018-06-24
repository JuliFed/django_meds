from django.contrib import admin
from .models import Category, SprService, Doctor


admin.site.register(Category)
admin.site.register(SprService)
admin.site.register(Doctor)