from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^formulario/',views.formulario, name='formulario'),
    url(r'^login/',views.login, name='login'),
    url(r'^$',views.index, name='index'),
]