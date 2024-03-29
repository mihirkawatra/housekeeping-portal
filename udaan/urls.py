"""udaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.shortcuts import redirect
from household.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view, name='index'),
    path("add-asset", AssetView.as_view(), name='add_asset'),
    path("add-task", TaskView.as_view(), name='add_task'),
    path("add-worker", WorkerView.as_view(), name='add_worker'),
    path("assets/all", assets_all, name='all_assets'),
    path("allocate-task", AllocateView.as_view(), name='allocate'),
    path("workers/all", workers_all, name='all_assets'),
    re_path(r"^worker/(?P<workerid>[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12})/$", worker_view, name='worker'),
]
