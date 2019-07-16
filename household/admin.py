from django.contrib import admin
from .models import Asset, Task, Worker, Allocation
from uuid import UUID
# Register your models here.
# admin.site.register([Asset, Task, Worker, Allocation])
@admin.register(Asset, Task, Worker)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'id')

def allocation_details(obj):
    worker = Worker.objects.filter(id = UUID(str(obj.worker_id))).values()[0]['name']
    task = Task.objects.filter(id = UUID(str(obj.task_id))).values()[0]['name']
    asset = Asset.objects.filter(id = UUID(str(obj.asset_id))).values()[0]['name']
    return worker+' - '+task+' - '+asset
@admin.register(Allocation)
class AllocAdmin(admin.ModelAdmin):
    list_display = (allocation_details,)
