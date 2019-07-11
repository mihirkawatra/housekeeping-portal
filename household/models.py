from django.db import models
import uuid
# Create your models here.
class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    def __str__(self):
        return str(self.id)

class Task(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                    = models.CharField(max_length=20)
    asset_id                = models.ForeignKey('Asset', on_delete=models.CASCADE, default=None, blank=True)
    worker_id               = models.ForeignKey('Worker', on_delete=models.CASCADE, default=None, blank=True)
    time_of_allocation      = models.DateTimeField(default=None, blank=True)
    task_to_be_performed_by = models.DateTimeField(default=None, blank=True)
    def __str__(self):
        return str(self.id)

class Worker(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                    = models.CharField(max_length=20)
    tasks                   = models.ManyToManyField('Task', blank=True, default=None)
    def __str__(self):
        return str(self.id)
