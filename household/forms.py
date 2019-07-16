from django import forms
from .models import Worker, Task, Asset, Allocation
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import SelectDateWidget
ASSET_TYPES = [
    ('object','Object'),
    ('place','Place')
]
class AssetForm(forms.Form):
    name = forms.CharField(label='Asset Name')
    type = forms.CharField(label='Asset Type', widget=forms.Select(choices=ASSET_TYPES))


TASK_FREQUENCIES = [
    ('hourly','Hourly'),
    ('daily','Daily'),
    ('weekly','Weekly'),
    ('monthly','Monthly'),
    ('yearly','Yearly'),
]
class TaskForm(forms.Form):
    name = forms.CharField(label='Task Name')
    frequency = forms.CharField(label='Asset Type', widget=forms.Select(choices=TASK_FREQUENCIES))

class WorkerForm(forms.Form):
    name = forms.CharField(label='Worker Name')

TASKS = [(str(obj["id"]), obj["name"]+' - '+obj["frequency"]) for obj in Task.objects.all().values()]
WORKERS = [(str(obj["id"]), obj["name"]) for obj in Worker.objects.all().values()]
ASSETS = [(str(obj["id"]), obj["name"]+' - '+obj["type"]) for obj in Asset.objects.all().values()]
class AllocationForm(forms.Form):
    task_id = forms.CharField(label='Task', widget = forms.Select(choices=TASKS))
    worker_id = forms.CharField(label='Worker', widget = forms.Select(choices=WORKERS))
    asset_id = forms.CharField(label='Asset', widget = forms.Select(choices=ASSETS))
    deadline = forms.DateTimeField(widget = SelectDateWidget())
