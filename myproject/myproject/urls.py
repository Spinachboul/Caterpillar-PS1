# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inspections/', include('inspections.urls')),  # Ensure this line is included
]
