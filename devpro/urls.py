

from django.contrib import admin
from django.urls import path
from devpro.encurtador import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>', views.redirecionar),
    path('relatorios/<slug:slug>', views.relatorios),
]
