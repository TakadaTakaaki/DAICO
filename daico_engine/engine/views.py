from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render

# user
def index(request):
    return render(request, 'user/home/index.html')

# _uuidで詳細はできると思ったのでファイル名_uuid.htmlにしました

# article 記事
def article(request):
    return render(request, 'user/article/index.html')
def article_detail(request):
    return render(request, 'user/article/_uuid.html')
# company 会社詳細
def company(request):
    return render(request, 'user/company/index.html')
def blog(request):
    return render(request, 'user/company/blog/index.html')
def blog_detail(request):
    return render(request, 'user/company/blog/_uuid.html')
def plan(request):
    return render(request, 'user/company/plan/index.html')
    # 裏側見てから決めるページを分けるのか表示方法でどうにかするのか
def review(request):
    return render(request, 'user/company/review/index.html')
def staff(request):
    return render(request, 'user/company/staff/index.html')
def staff_detail(request):
    return render(request, 'user/company/staff/_uuid.html')
# chat お問い合わせ user⇔company
def chat(request):
    return render(request, 'user/chat/index.html')
# favorite お気に入り
def favorite(request):
    return render(request, 'user/favorite/index.html')
# login ログイン画面
def login(request):
    return render(request, 'user/login/index.html')
# notice 通知
def notice_company(request):
    return render(request, 'user/notice/company/index.html')
def notice_company_detail(request):
    return render(request, 'user/notice/company/_uuid.html')
def notice_engine(request):
    return render(request, 'user/notice/engine/index.html')
def notice_engine_detail(request):
    return render(request, 'user/notice/engine/_uuid.html')
# order 注文履歴
def order(request):
    return render(request, 'user/order/index.html')
def order_detail(request):
    return render(request, 'user/order/_uuid.html')
def order_cancel(request):
    return render(request, 'user/order/cancel/index.html')
def order_cancel_detail(request):
    return render(request, 'user/order/cancel/_uuid.html')
def order_notExecuted(request):
    return render(request, 'user/order/notExecuted/index.html')
def order_notExecuted_detail(request):
    return render(request, 'user/order/notExecuted/_uuid.html')
# register 新規登録
def register(request):
    return render(request, 'user/register/index.html')
def register_detail(request):
    return render(request, 'user/register/_uuid.html')
# reserve 予約
def reserve(request):
    return render(request, 'user/reserve/index.html')
def reserve_date(request):
    return render(request, 'user/reserve/date/index.html')
def reserve_date_detail(request):
    return render(request, 'user/reserve/date/_uuid.html')
def reserve_payment(request):
    return render(request, 'user/reserve/payment/index.html')
def reserve_payment_detail(request):
    return render(request, 'user/reserve/payment/_uuid.html')
def reserve_done(request):
    return render(request, 'user/reserve/done/index.html')
# search 検索
def search(request):
    return render(request, 'user/search/index.html')
# setting 設定
def setting(request):
    return render(request, 'user/setting/index.html')
def setting_companyInquiry(request):
    return render(request, 'user/setting/companyInquiry/index.html')
def setting_contact(request):
    return render(request, 'user/setting/contact/index.html')
# creditについては変更と追加ができないとだめだと思います
def setting_credit(request):
    return render(request, 'user/setting/credit/index.html')
def setting_creditAdd(request):
    return render(request, 'user/setting/credit/creditAdd.html')
def setting_creditEdit(request):
    return render(request, 'user/setting/credit/creditEdit.html')
def setting_hidden(request):
    return render(request, 'user/setting/hidden/index.html')
def setting_tpoint(request):
    return render(request, 'user/setting/tpoint/index.html')
def setting_unsubscribe(request):
    return render(request, 'user/setting/unsubscribe/index.html')
def setting_userDetailChange(request):
    return render(request, 'user/setting/userDetailChange/index.html')


# company
# engine
