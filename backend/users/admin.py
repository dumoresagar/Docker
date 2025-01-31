from django.contrib import admin
from users.models import (User,)
from .forms import UserCreationForm
from import_export.admin import ImportExportModelAdmin
from django import forms

class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    form = UserCreationForm
    list_display = [
        'id', 'username', 'email',
        'date_created', 'date_updated', 'active_status','is_deleted',  
    ]
    list_display_links=['id','username']
    exclude = ['peram_group']







admin.site.register(User,UserAdmin)
