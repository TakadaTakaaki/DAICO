"""daico_engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# 下二つが画像関連の場所と繋いでる


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('app.urls')),
    url(r'article/', include('app.urls')),
    url(r'adetail/', include('app.urls')),
    # article_detail
    url(r'enterprise/', include('app.urls')),
    url(r'blog/', include('app.urls')),
    url(r'bdetail/', include('app.urls')),
    # blog_detail
    url(r'plan/', include('app.urls')),
    url(r'review/', include('app.urls')),
    url(r'staff/', include('app.urls')),
    url(r'sdetail/', include('app.urls')),
    # staff_detail
    url(r'chat/', include('app.urls')),
    url(r'favorite/', include('app.urls')),
    url(r'notice_c/', include('app.urls')),
    # nptice_company
    url(r'ncdetail/', include('app.urls')),
    # notice_company_detail
    url(r'nengine/', include('app.urls')),
    # notice_engine
    url(r'nedetail/', include('app.urls')),
    # notice_engine_detail
    url(r'order/', include('app.urls')),
    url(r'odetail/', include('app.urls')),
    # order_detail
    url(r'cancel/', include('app.urls')),
    # order_cancel
    url(r'ocdetail/', include('app.urls')),
    # order_cancel_detail
    url(r'onotExecuted/', include('app.urls')),
    # order_notExecuted
    url(r'ondetail/', include('app.urls')),
    # order_notExecuted_detail
    url(r'register/', include('app.urls')),
    url(r'rdetail/', include('app.urls')),
    # register_detail
    url(r'reserve/', include('app.urls')),
    url(r'rdate/', include('app.urls')),
    # reserve_date
    url(r'rddetail/', include('app.urls')),
    # reserve_date_detail
    url(r'rpayment/', include('app.urls')),
    # reserve_payment
    url(r'rpdetail/', include('app.urls')),
    # reserve_payment_detail
    url(r'rconfirmation/', include('app.urls')),
    # reserve_confirmation
    url(r'rdone/', include('app.urls')),
    # reserve_done
    url(r'search/', include('app.urls')),
    url(r'setting/', include('app.urls')),    
    url(r'sinquiry/', include('app.urls')),
    # setting_companyInquiry
    url(r'scontact/', include('app.urls')),
    # setting_contact
    url(r'scredit/', include('app.urls')),
    # setting_credit
    url(r'screditAdd/', include('app.urls')),
    # setting_creditAdd
    url(r'screditEdit/', include('app.urls')),
    # setting_creditEdit
    url(r'shidden/', include('app.urls')),
    # setting_hidden
    url(r'stpoint/', include('app.urls')),
    # setting_tpoint
    url(r'sunsubscribe/', include('app.urls')),
    # setting_unsubscribe
    url(r'suserDetailChange/', include('app.urls')),
    # setting_userDetailChange

    # company
    url(r'company/', include('app.urls')),
    url(r'booking/', include('app.urls')),
    url(r'bookdetail/', include('app.urls')),
    url(r'coupon/', include('app.urls')),
    url(r'player/', include('app.urls')),
    url(r'medetail/', include('app.urls')),
    url(r'read/', include('app.urls')),
    url(r'redetail/', include('app.urls')),
    url(r'valuation/', include('app.urls')),
    url(r'compilation/', include('app.urls')),
    url(r'compon/', include('app.urls')),
    url(r'complay/', include('app.urls')),
    url(r'cmdetail/', include('app.urls')),
    url(r'comre/', include('app.urls')),
    url(r'comvalua/', include('app.urls')),
    url(r'survey/', include('app.urls')),
    url(r'voice/', include('app.urls')),
    url(r'vcdetail/', include('app.urls')),
    url(r'vedetail/', include('app.urls')),


    # engine
    url(r'engine/', include('app.urls')),
    url(r'analytics/', include('app.urls')),
    url(r'contact/', include('app.urls')),
    url(r'client/', include('app.urls')),
    url(r'inquire/', include('app.urls')),
    url(r'customer/', include('app.urls')),
    url(r'guest/', include('app.urls')),
    url(r'gdetail/', include('app.urls')),
    url(r'edit/', include('app.urls')),
    url(r'manage/', include('app.urls')),
    url(r'mdetail/', include('app.urls')),
    url(r'publish/', include('app.urls')),
    url(r'pdetail/', include('app.urls')),
    url(r'diary/', include('app.urls')),
    url(r'ddetail/', include('app.urls')),
    url(r'employ/', include('app.urls')),
    url(r'xdetail/', include('app.urls')),
    url(r'menu/', include('app.urls')),
    url(r'rate/', include('app.urls')),
    url(r'write/', include('app.urls')),
    url(r'wdetail/', include('app.urls')),
    url(r'category/', include('app.urls')),
    # 引数をループさせない
    url(r'', include('app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 画像追加に必要
