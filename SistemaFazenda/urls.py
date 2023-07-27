from django.contrib import admin
from django.urls import path, include
from Gado import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', RedirectView.as_view(url='/dashboard/')),
    path('', include('admin_material.urls')),
]
