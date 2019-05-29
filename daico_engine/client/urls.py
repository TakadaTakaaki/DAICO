from django.conf.urls import url
from django.urls import path
from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/

urlpatterns = [
    # ex: /accounts/signup/
    # path('signup/', views.SignUpView.as_view(), name='signup'),
        # company
    url(r'company', views.company, name="company"),
    url(r'booking', views.booking, name="booking"),
    url(r'bookdetail', views.bookdetail, name="bookdetail"),
    url(r'coupon', views.coupon, name="coupon"),
    url(r'player', views.player, name="player"),
    url(r'medetail', views.medetail, name="medetail"),
    url(r'read', views.read, name="read"),
    url(r'redetail', views.redetail, name="redetail"),
    url(r'valuation', views.valuation, name="valuation"),
    url(r'compilation', views.compilation, name="compilation"),
    url(r'hensyu', views.hensyu, name="hensyu"),
    url(r'compon', views.compon, name="compon"),
    url(r'complay', views.complay, name="complay"),
    url(r'cmdetail', views.cmdetail, name="cmdetail"),
    url(r'comre', views.comre, name="comre"),
    url(r'comvalua', views.comvalua, name="comvalua"),
    url(r'survey', views.survey, name="survey"),
    url(r'voice', views.voice, name="voice"),
    url(r'vcdetail', views.vcdetail, name="vcdetail"),
    url(r'vedetail', views.vedetail, name="vedetail"),
    path('compilation/<int:pk>/', views.compilation, name="compilation"),
    # path('compilation/<int:pk>/', views.compilation, name="compilation"),
]