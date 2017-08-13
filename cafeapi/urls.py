from django.conf.urls import url
from cafeapi import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Cafe API')

urlpatterns = [
    url(r'^cafeapi/schema/$', schema_view, name='schema'),
    url(r'^cafeapi/contas/(?P<cliente>[0-9]+)/$', views.ContaList.as_view()),
    url(r'^cafeapi/conta(?P<id>[0-9]+)/$', views.ContaDetail.as_view()),
    url(r'^cafeapi/clientes/$', views.ClienteList.as_view()),
    url(r'^cafeapi/cliente/(?P<id_cli>[0-9]+)/S', views.ClienteDetail.as_view()),
    url(r'^cafeapi/maquinas/$', views.MaquinaList.as_view()),
    url(r'^cafeapi/maquina/(?P<maq>[0-9]+)/$', views.MaquinaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
