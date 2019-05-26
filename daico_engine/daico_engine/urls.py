from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# 下二つが画像関連の場所と繋いでる


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('customer.urls')),

    # user
    path('customer/', include('customer.urls')),
    url(r'article/', include('customer.urls')),
    url(r'adetail/', include('customer.urls')),
    url(r'type/', include('customer.urls')),
    # article_detail
    url(r'enterprise/', include('customer.urls')),
    url(r'blog/', include('customer.urls')),
    url(r'bdetail/', include('customer.urls')),
    # blog_detail
    url(r'plan/', include('customer.urls')),
    url(r'review/', include('customer.urls')),
    url(r'staff/', include('customer.urls')),
    url(r'sdetail/', include('customer.urls')),
    # staff_detail
    url(r'chat/', include('customer.urls')),
    url(r'fav/', include('customer.urls')),
    url(r'notice_c/', include('customer.urls')),
    # nptice_company
    url(r'ncdetail/', include('customer.urls')),
    # notice_company_detail
    url(r'nengine/', include('customer.urls')),
    # notice_engine
    url(r'nedetail/', include('customer.urls')),
    # notice_engine_detail
    url(r'order/', include('customer.urls')),
    url(r'odetail/', include('customer.urls')),
    # order_detail
    url(r'cancel/', include('customer.urls')),
    # order_cancel
    url(r'ocdetail/', include('customer.urls')),
    # order_cancel_detail
    url(r'onotExecuted/', include('customer.urls')),
    # order_notExecuted
    url(r'ondetail/', include('customer.urls')),
    # order_notExecuted_detail
    url(r'register/', include('customer.urls')),
    url(r'rdetail/', include('customer.urls')),
    # register_detail
    url(r'reserve/', include('customer.urls')),
    url(r'rdate/', include('customer.urls')),
    # reserve_date
    url(r'rddetail/', include('customer.urls')),
    # reserve_date_detail
    url(r'rpayment/', include('customer.urls')),
    # reserve_payment
    url(r'rpdetail/', include('customer.urls')),
    # reserve_payment_detail
    url(r'rconfirmation/', include('customer.urls')),
    # reserve_confirmation
    url(r'rdone/', include('customer.urls')),
    # reserve_done
    url(r'search/', include('customer.urls')),
    url(r'setting/', include('customer.urls')),    
    url(r'sinquiry/', include('customer.urls')),
    # setting_companyInquiry
    url(r'scontact/', include('customer.urls')),
    # setting_contact
    url(r'scredit/', include('customer.urls')),
    # setting_credit
    url(r'screditAdd/', include('customer.urls')),
    # setting_creditAdd
    url(r'screditEdit/', include('customer.urls')),
    # setting_creditEdit
    url(r'shidden/', include('customer.urls')),
    # setting_hidden
    url(r'stpoint/', include('customer.urls')),
    # setting_tpoint
    url(r'sunsubscribe/', include('customer.urls')),
    # setting_unsubscribe
    url(r'suserDetailChange/', include('customer.urls')),
    # setting_userDetailChange
    url(r'uuiuserDetailChange/', include('customer.urls')),
    # setting_userDetailChange_uuid
    url(r'login/', include('customer.urls')),
    # login
    url(r'logout/', include('customer.urls')),
    # logout
    url(r'', include('customer.urls')),


    # company
    path('client/', include('client.urls')),
    url(r'company/', include('client.urls')),
    url(r'booking/', include('client.urls')),
    url(r'bookdetail/', include('client.urls')),
    url(r'coupon/', include('client.urls')),
    url(r'player/', include('client.urls')),
    url(r'medetail/', include('client.urls')),
    url(r'read/', include('client.urls')),
    url(r'redetail/', include('client.urls')),
    url(r'valuation/', include('client.urls')),
    url(r'compilation/', include('client.urls')),
    url(r'compon/', include('client.urls')),
    url(r'complay/', include('client.urls')),
    url(r'cmdetail/', include('client.urls')),
    url(r'comre/', include('client.urls')),
    url(r'comvalua/', include('client.urls')),
    url(r'survey/', include('client.urls')),
    url(r'voice/', include('client.urls')),
    url(r'vcdetail/', include('client.urls')),
    url(r'vedetail/', include('client.urls')),
    url(r'', include('client.urls')),



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

    #　ログイン練習
    # url(r'polls/', include('app.urls')), 
    # url(r'user-base/', include('customer.urls')), 
    # 引数をループさせない
    url(r'', include('app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 画像追加に必要
