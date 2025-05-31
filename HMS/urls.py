from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('doctors/', include('doctor.urls')),
    path('patients/', include('patient.urls')),
]
