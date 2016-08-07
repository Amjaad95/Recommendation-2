from django.contrib import admin

from .models import Recommendation, Category

admin.site.register(Recommendation)
admin.site.register(Category)