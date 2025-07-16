from django.contrib import admin
from django.urls import path
from k8sapp.views import k8s_info_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', k8s_info_view, name='k8s-info'),
]
