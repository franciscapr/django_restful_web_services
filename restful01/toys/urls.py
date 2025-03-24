from django.conf.urls import url
from toys import views

urlpatterns = [
    url(r'^toys/$', views.toys_list),
    url(r'^toys/(?P<pk>[0-9]+)$', views.toys_detail),
]