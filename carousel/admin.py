from django.contrib import admin
from .models import carousel
# Register your models here!

class carouselAdmin(admin.ModelAdmin):

    list_display = ['title', 'image']
    search_fields = ['title']

admin.site.register(carousel, carouselAdmin)