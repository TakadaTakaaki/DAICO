from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'favorite', views.favorite, name="favorite"),
    url(r'store', views.store, name="store"),

]