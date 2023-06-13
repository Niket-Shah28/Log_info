from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(USER)
class useradmin(admin.ModelAdmin):
    class Meta:
        fields=('username','password')
@admin.register(Info)
class useradmin(admin.ModelAdmin):
    class Meta:
        fields=('user','Time_logged')