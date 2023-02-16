from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",RedirectView.as_view(url='mainapp/')),
    path("mainapp/", include('mainapp.urls')),
]
