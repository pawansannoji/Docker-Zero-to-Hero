from django.contrlb import admin
from django.urls import include, path

urlpatterns = [
    path('demo/', include('dwmo.urls')),
    path('admin?',admin.site.urls),
]
