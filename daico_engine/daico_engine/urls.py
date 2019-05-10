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
    url(r'^$', include('app.urls')),
    url(r'article/', include('app.urls')),
    url(r'article_detail/', include('app.urls')),
    url(r'company/', include('app.urls')),
    url(r'blog/', include('app.urls')),
    url(r'blog_detail/', include('app.urls')),
    url(r'plan/', include('app.urls')),
    url(r'review/', include('app.urls')),
    url(r'staff/', include('app.urls')),
    url(r'staff_detail/', include('app.urls')),
    url(r'chat/', include('app.urls')),
    url(r'favorite/', include('app.urls')),
    url(r'notice_company/', include('app.urls')),
    url(r'notice_company_detail/', include('app.urls')),
    url(r'notice_engine/', include('app.urls')),
    url(r'notice_engine_detail/', include('app.urls')),
    url(r'order/', include('app.urls')),
    url(r'order_detail/', include('app.urls')),
    url(r'order_cancel/', include('app.urls')),
    url(r'order_cancel_detail/', include('app.urls')),
    url(r'order_notExecuted/', include('app.urls')),
    url(r'order_notExecuted_detail/', include('app.urls')),
    url(r'register/', include('app.urls')),
    url(r'register_detail/', include('app.urls')),
    url(r'reserve/', include('app.urls')),
    url(r'reserve_date/', include('app.urls')),
    url(r'reserve_date_detail/', include('app.urls')),
    url(r'reserve_payment/', include('app.urls')),
    url(r'reserve_payment_detail/', include('app.urls')),
    url(r'reserve_done/', include('app.urls')),
    url(r'search/', include('app.urls')),
    url(r'setting/', include('app.urls')),    
    url(r'setting_companyInquiry/', include('app.urls')),
    url(r'setting_contact/', include('app.urls')),
    url(r'setting_credit/', include('app.urls')),
    url(r'setting_creditAdd/', include('app.urls')),
    url(r'setting_creditEdit/', include('app.urls')),
    url(r'setting_hidden/', include('app.urls')),
    url(r'setting_tpoint/', include('app.urls')),
    url(r'setting_unsubscribe/', include('app.urls')),
    url(r'setting_userDetailChange/', include('app.urls')),

    # company
    # engine
    url(r'', include('app.urls')),
]
