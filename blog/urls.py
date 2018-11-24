from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^formulario/',views.formulario, name='formulario'),
    url(r'^login/',views.login, name='login'),
    url(r'^$',views.index, name='index'),
    url(r'^Mantenimiento/',views.formuMantenimiento, name='formuMantenimiento'),
    url(r'^arrendarMapa/',views.arrendarMapa, name='arrendarMapa'),
    url(r'^arrendar/',views.arrendar, name='arrendar'),
    url(r'^arrendarPositivo/',views.arrendarPosito, name='arrendarPosito'),
]