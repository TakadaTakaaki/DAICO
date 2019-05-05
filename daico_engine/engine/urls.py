from django.conf.urls import url
from . import views
 
urlpatterns = [
    # user
    url(r'^$', views.index, name='index'),
    url(r'article', views.article, name="article"),
    url(r'article_detail', views.article_detail, name="article_detail"),
    url(r'company', views.company, name="company"),
    url(r'blog', views.blog, name="blog"),
    url(r'blog_detail', views.blog_detail, name="blog_detail"),
    url(r'plan', views.plan, name="plan"),
    url(r'review', views.review, name="review"),
    url(r'staff', views.staff, name="staff"),
    url(r'staff_detail', views.staff_detail, name="staff_detail"),
    url(r'chat', views.chat, name="chat"),
    url(r'favorite', views.favorite, name="favorite"),
    url(r'notice_company', views.notice_company, name="notice_company"),
    url(r'notice_company_detail', views.notice_company_detail, name="notice_company_detail"),
    url(r'notice_engine', views.notice_engine, name="notice_engine"),
    url(r'notice_engine_detail', views.notice_engine_detail, name="notice_engine_detail"),
    url(r'order', views.order, name="order"),
    url(r'order_detail', views.order_detail, name="order_detail"),
    url(r'order_cancel', views.order_cancel, name="order_cancel"),
    url(r'order_cancel_detail', views.order_cancel_detail, name="order_cancel_detail"),
    url(r'order_notExecuted', views.order_notExecuted, name="order_notExecuted"),
    url(r'order_notExecuted_detail', views.order_notExecuted_detail, name="order_notExecuted_detail"),
    url(r'register', views.register, name="register"),
    url(r'register_detail', views.register_detail, name="register_detail"),
    url(r'reserve', views.reserve, name="reserve"),
    url(r'reserve_date', views.reserve_date, name="reserve_date"),
    url(r'reserve_date_detail', views.reserve_date_detail, name="reserve_date_detail"),
    url(r'reserve_payment', views.reserve_payment, name="reserve_payment"),
    url(r'reserve_payment_detail', views.reserve_payment_detail, name="reserve_payment_detail"),
    url(r'reserve_done', views.reserve_done, name="reserve_done"),
    url(r'search', views.search, name="search"),
    url(r'setting', views.setting, name="setting"),
    url(r'setting_companyInquiry', views.setting_companyInquiry, name="setting_companyInquiry"),
    url(r'setting_contact', views.setting_contact, name="setting_contact"),
    url(r'setting_credit', views.setting_credit, name="setting_credit"),
    url(r'setting_creditAdd', views.setting_creditAdd, name="setting_creditAdd"),
    url(r'setting_creditEdit', views.setting_creditEdit, name="setting_creditEdit"),
    url(r'setting_hidden', views.setting_hidden, name="setting_hidden"),
    url(r'setting_tpoint', views.setting_tpoint, name="setting_tpoint"),
    url(r'setting_unsubscribe', views.setting_unsubscribe, name="setting_unsubscribe"),
    url(r'setting_userDetailChange', views.setting_userDetailChange, name="setting_userDetailChange"),
    
    # company
    # engine

]