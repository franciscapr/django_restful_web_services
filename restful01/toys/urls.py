from django.urls import path, re_path, include
from toys import views

urlpatterns = [
    path('toys/', views.toy_list),
    re_path(r'^toys/(?P<pk>[0-9]+)$', views.toy_detail),    # re_path es para el regex
]