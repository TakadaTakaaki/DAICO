from django.conf.urls import url
from django.urls import path
from django.core.exceptions import MultipleObjectsReturned
from . import views

urlpatterns = [
    # engine
    url(r'engine', views.engine, name="engine"),
    url(r'analytics', views.analytics, name="analytics"),
    url(r'contact', views.contact, name="contact"),
    url(r'client', views.client, name="client"),
    url(r'inquire', views.inquire, name="inquire"),
    url(r'customer', views.customer, name="customer"),
    url(r'guest', views.guest, name="guest"),
    url(r'gdetail', views.gdetail, name="gdetail"),
    url(r'edit', views.edit, name="edit"),
    url(r'manage', views.manage, name="manage"),
    url(r'mdetail', views.mdetail, name="mdetail"),
    url(r'publish', views.publish, name="publish"),
    url(r'pdetail', views.pdetail, name="pdetail"),
    url(r'diary', views.diary, name="diary"),
    url(r'ddetail', views.ddetail, name="ddetail"),
    url(r'employ', views.employ, name="employ"),
    url(r'xdetail', views.xdetail, name="xdetail"),
    url(r'menu', views.menu, name="menu"),
    url(r'rate', views.rate, name="rate"),
    url(r'write', views.write, name="write"),
    path('wdetail/<int:pk>/', views.wdetail, name="wdetail"),
    path('category/<int:category_id>/', views.category, name="category"),
]