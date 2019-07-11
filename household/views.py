from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden,HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from .models import Asset, Task, Worker
# Create your views here.
def index_view(request):
    return HttpResponse("<h1> Hello </h1>")

def add_asset(request):
    return HttpResponse("<h1> Hello </h1>")

def add_task(request):
    return HttpResponse("<h1> Hello </h1>")

def add_worker(request):
    return HttpResponse("<h1> Hello </h1>")

def assets_all(request):
    return HttpResponse("<h1> Hello </h1>")

def task_allocate(request):
    return HttpResponse("<h1> Hello </h1>")

def worker_view(request, workerid):
    try:
        obj = Worker.objects.get(id=workerid)
        print(obj.name)
        return HttpResponse(f"<h1> Hello { obj.name }</h1>")
    except Worker.DoesNotExist:
        return HttpResponse(f"<h1>Worker not found</h1>")
