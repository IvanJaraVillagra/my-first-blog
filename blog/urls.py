from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^formulario/',views.formulario, name='formulario'),
    url(r'^login/',views.login, name='login'),
    url(r'^$',views.index, name='index'),
    url(r'^mantenimiento/',views.formuMantenimiento, name='formuMantenimiento'),
    url(r'^arrendarMapa/',views.arrendarMapa, name='arrendarMapa'),
    url(r'^arrendar/',views.arrendar, name='arrendar'),
    url(r'^arrendaar/',views.arrendarPosito, name='arrendarPosito'),
    url(r'^terminar/',views.terminarArriendo, name='terminarArriendo'),
    url(r'^agradecimientos/',views.graciasportodo, name='graciasportodo'),
]