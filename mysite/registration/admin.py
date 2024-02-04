from django.contrib import admin
from .models import Registration
# Register your models here.
@admin.register(Registration)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    search_fields = ['name','email']
    