from django.contrib import admin
from .models import Lot

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=('title','text','tracking_code')

admin.site.register(Lot,AuthorAdmin)