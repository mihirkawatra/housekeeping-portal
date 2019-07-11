from django.contrib import admin
from .models import Asset, Task, Worker
# Register your models here.

admin.site.register([Asset, Task, Worker])
