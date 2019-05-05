from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render

# user
def index(request):
    return render(request, 'user/home/home.html')

# 基本_detail系はあとで_uuid作成してリンクさせるはず

# article 記事
def article(request):
    return render(request, 'user/article/article.html')
def article_detail(request):
    return render(request, 'user/article/article_detail.html')
# company 会社詳細
def company(request):
    return render(request, 'user/company/company.html')
def blog(request):
    return render(request, 'user/company/blog/blog.html')
def blog_detail(request):
    return render(request, 'user/company/blog/blog_detail.html')
def plan(request):
    return render(request, 'user/company/plan/plan.html')
    # 裏側見てから決めるページを分けるのか表示方法でどうにかするのか
def review(request):
    return render(request, 'user/company/review/review.html')
def staff(request):
    return render(request, 'user/company/staff/staff.html')
def staff_detail(request):
    return render(request, 'user/company/staff/staff_detail.html')
# chat お問い合わせ user⇔company
def chat(request):
    return render(request, 'user/chat/chat.html')
# favorite お気に入り
def favorite(request):
    return render(request, 'user/favorite/favorite.html')
# login ログイン画面
def login(request):
    return render(request, 'user/login/login.html')
# notice 通知
def notice_company(request):
    return render(request, 'user/notice/company/company.html')
def notice_company_detail(request):
    return render(request, 'user/notice/company/company_detail.html')
def notice_engine(request):
    return render(request, 'user/notice/engine/engine.html')
def notice_engine_detail(request):
    return render(request, 'user/notice/engine/engine_detail.html')
# order 注文履歴
def order(request):
    return render(request, 'user/order/order.html')
def order_detail(request):
    return render(request, 'user/order/order_detail.html')
def order_cancel(request):
    return render(request, 'user/order/cancel/cancel.html')
def order_cancel_detail(request):
    return render(request, 'user/order/cancel/cancel_detail.html')
def order_notExecuted(request):
    return render(request, 'user/order/notExecuted/notExecuted.html')
def order_notExecuted_detail(request):
    return render(request, 'user/order/notExecuted/notExecuted_detail.html')
# register 新規登録
def register(request):
    return render(request, 'user/register/register.html')
def register_detail(request):
    return render(request, 'user/register/register_detail.html')
# reserve 予約
def reserve(request):
    return render(request, 'user/reserve/reserve.html')
def reserve_date(request):
    return render(request, 'user/reserve/date/date.html')
def reserve_date_detail(request):
    return render(request, 'user/reserve/date/date_detail.html')
def reserve_payment(request):
    return render(request, 'user/reserve/payment/payment.html')
def reserve_payment_detail(request):
    return render(request, 'user/reserve/payment/payment_detail.html')
def reserve_done(request):
    return render(request, 'user/reserve/done/done.html')
# search 検索
def search(request):
    return render(request, 'user/search/search.html')
# setting 設定
def setting_companyInquiry(request):
    return render(request, 'user/setting/companyInquiry/companyInquiry.html')
def setting_contact(request):
    return render(request, 'user/setting/contact/contact.html')
# creditについては変更と追加ができないとだめだと思います
def setting_credit(request):
    return render(request, 'user/setting/credit/credit.html')
def setting_creditAdd(request):
    return render(request, 'user/setting/credit/creditAdd.html')
def setting_creditEdit(request):
    return render(request, 'user/setting/credit/creditEdit.html')
def setting_hidden(request):
    return render(request, 'user/setting/hidden/hidden.html')
def setting_tpoint(request):
    return render(request, 'user/setting/tpoint/tpoint.html')
def setting_unsubscribe(request):
    return render(request, 'user/setting/unsubscribe/unsubscribe.html')
def setting_userDetailChange(request):
    return render(request, 'user/setting/userDetailChange/userDetailChange.html')


# company
# engine
