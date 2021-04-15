from django.conf.urls import url
from myapp import views
urlpatterns = [

    url(r'^registration$',views.registration_list),
    url(r'^registration/(?P<pk>[0-9]+)$', views.registration)
]