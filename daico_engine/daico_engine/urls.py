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
# from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('engine.urls')),
    url(r'article/', include('engine.urls')),
    url(r'article_detail/', include('engine.urls')),
    url(r'company/', include('engine.urls')),
    url(r'blog/', include('engine.urls')),
    url(r'blog_detail/', include('engine.urls')),
    url(r'plan/', include('engine.urls')),
    url(r'review/', include('engine.urls')),
    url(r'staff/', include('engine.urls')),
    url(r'staff_detail/', include('engine.urls')),
    url(r'chat/', include('engine.urls')),
    url(r'favorite/', include('engine.urls')),
    url(r'login/', include('engine.urls')),
    url(r'notice_company/', include('engine.urls')),
    url(r'notice_company_detail/', include('engine.urls')),
    url(r'notice_engine/', include('engine.urls')),
    url(r'notice_engine_detail/', include('engine.urls')),
    url(r'order/', include('engine.urls')),
    url(r'order_detail/', include('engine.urls')),
    url(r'order_cancel/', include('engine.urls')),
    url(r'order_cancel_detail/', include('engine.urls')),
    url(r'order_notExecuted/', include('engine.urls')),
    url(r'order_notExecuted_detail/', include('engine.urls')),
    url(r'register/', include('engine.urls')),
    url(r'register_detail/', include('engine.urls')),
    url(r'reserve/', include('engine.urls')),
    url(r'reserve_date/', include('engine.urls')),
    url(r'reserve_date_detail/', include('engine.urls')),
    url(r'reserve_payment/', include('engine.urls')),
    url(r'reserve_payment_detail/', include('engine.urls')),
    url(r'reserve_done/', include('engine.urls')),
    url(r'search/', include('engine.urls')),
    url(r'setting_companyInquiry/', include('engine.urls')),
    url(r'setting_contact/', include('engine.urls')),
    url(r'setting_credit/', include('engine.urls')),
    url(r'setting_creditAdd/', include('engine.urls')),
    url(r'setting_creditEdit/', include('engine.urls')),
    url(r'setting_hidden/', include('engine.urls')),
    url(r'setting_tpoint/', include('engine.urls')),
    url(r'setting_unsubscribe/', include('engine.urls')),
    url(r'setting_userDetailChange/', include('engine.urls')),

    # company
    # engine
    url(r'', include('engine.urls')),
]
