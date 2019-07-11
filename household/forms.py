from django import forms

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
