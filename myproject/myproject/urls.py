"""myproject URL Configuration"""

from django.contrib import admin
from django.urls import path, include  # use include and path only

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # replace url() with path()
]
