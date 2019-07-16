from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import FormView
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from .models import Asset, Task, Worker, Allocation
from .forms import AssetForm, TaskForm, WorkerForm, AllocationForm
from datetime import datetime
from uuid import UUID

def index_view(request):
    return render(request,'housekeeping/index.html')

class AssetView(FormView):
    template_name = 'housekeeping/form.html'
    form_class = AssetForm
    success_url = './'

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(AssetView, self).get_context_data(**kwargs)
        context['action'] = 'add_asset'
        return context

    def post(self, request, *args, **kwargs):
        print("Form Received")
        form = AssetForm(request.POST)
        return self.form_valid(form)
        print("Posted")

    def form_valid(self, form):
        print(form)
        name = form.cleaned_data.get("name")
        type = form.cleaned_data.get("type")
        Asset.objects.create(name=name,type=type)
        return super().form_valid(form)

class TaskView(FormView):
    template_name = 'housekeeping/form.html'
    form_class = TaskForm
    success_url = './'

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(TaskView, self).get_context_data(**kwargs)
        context['action'] = 'add_task'
        return context

    def post(self, request, *args, **kwargs):
        print("Form Received")
        form = TaskForm(request.POST)
        return self.form_valid(form)
        print("Posted")

    def form_valid(self, form):
        print(form)
        name = form.cleaned_data.get("name")
        frequency = form.cleaned_data.get("frequency")
        Task.objects.create(name=name,frequency=frequency)
        return super().form_valid(form)

class WorkerView(FormView):
    template_name = 'housekeeping/form.html'
    form_class = WorkerForm
    success_url = './'

    def get_context_data(self, **kwargs):
        """Use this to add extra context."""
        context = super(WorkerView, self).get_context_data(**kwargs)
        context['action'] = 'add_worker'
        return context

    def post(self, request, *args, **kwargs):
        print("Form Received")
        form = WorkerForm(request.POST)
        return self.form_valid(form)
        print("Posted")

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data)
        name = form.cleaned_data.get("name")
        Worker.objects.create(name=name)
        return super().form_valid(form)

def assets_all(request):
    assets = Asset.objects.all()
    return render(request,'housekeeping/listall.html', context={'list' : assets, 'name': 'Assets'})

# def task_allocate(request):
#     return render(request,'housekeeping/allocation.html', context={'form': AllocationForm})

class AllocateView(FormView):
    template_name = 'housekeeping/allocation.html'
    form_class = AllocationForm
    success_url = './'

    def post(self, request, *args, **kwargs):
        form = AllocationForm(request.POST)
        print("Form Received")
        return self.form_valid(form)

    def form_valid(self, form):
        print(form)
        worker_id = form.cleaned_data.get("worker_id")
        asset_id = form.cleaned_data.get("asset_id")
        task_id = form.cleaned_data.get("task_id")
        deadline = str(datetime.strptime(str(form.cleaned_data.get("deadline")).split('+')[0], '%Y-%m-%d %H:%M:%S').date())
        worker = Worker.objects.filter(id = UUID(str(worker_id)))[0]
        task = Task.objects.filter(id = UUID(str(task_id)))[0]
        asset = Asset.objects.filter(id = UUID(str(asset_id)))[0]
        Allocation.objects.create(asset_id=asset, task_id=task, worker_id=worker, task_to_be_performed_by=deadline)
        return super().form_valid(form)

def workers_all(request):
    workers = Worker.objects.all()
    return render(request,'housekeeping/listall.html', context={'list' : workers, 'name': 'Workers'})

def worker_view(request, workerid):
    try:
        obj = Worker.objects.get(id=workerid)
        tasks = Allocation.objects.filter(worker_id = obj.id).distinct()
        t = []
        for i in range(len(tasks.values())):
            curr_task = Task.objects.filter(id = tasks.values()[i]['task_id_id']).distinct().values()[0]
            curr_asset = Asset.objects.filter(id = tasks.values()[i]['asset_id_id']).distinct().values()[0]
            dic = tasks.values()[i]
            dic['name'] = curr_task['name']
            dic['frequency'] = curr_task['frequency']
            dic['asset_name'] = curr_asset['name']
            t.append(dic)
    except Worker.DoesNotExist:
        raise Http404("Worker Does Not Exist")
    return render(request,'housekeeping/view.html', context={'tasks' : t, 'name' : str(obj.name)})
