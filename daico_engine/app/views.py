from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from django.views import generic
from .models import Post,Category
from django.core.exceptions import MultipleObjectsReturned

# user
def index(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'user/home/index.html', {'posts': posts})

# _uuidで詳細はできると思ったのでファイル名_uuid.htmlにしました

# article 記事
def article(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'user/article/index.html', {'posts': posts})
def adetail(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, 'user/article/_uuid.html', {'posts': posts})
# company 会社詳細
def enterprise(request):
    return render(request, 'user/enterprise/index.html')
def blog(request):
    return render(request, 'user/enterprise/blog/index.html')
def bdetail(request):
    return render(request, 'user/enterprise/blog/_uuid.html')
def plan(request):
    return render(request, 'user/enterprise/plan/index.html')
    # 裏側見てから決めるページを分けるのか表示方法でどうにかするのか
def review(request):
    return render(request, 'user/enterprise/review/index.html')
def staff(request):
    return render(request, 'user/enterprise/staff/index.html')
def sdetail(request):
    return render(request, 'user/enterprise/staff/_uuid.html')
# chat お問い合わせ user⇔company
def chat(request):
    return render(request, 'user/chat/index.html')
# favorite お気に入り
def favorite(request):
    return render(request, 'user/favorite/index.html')
# notice 通知
def notice_c(request):
    return render(request, 'user/notice/company/index.html')
def ncdetail(request):
    return render(request, 'user/notice/company/_uuid.html')
def nengine(request):
    return render(request, 'user/notice/engine/index.html')
def nedetail(request):
    return render(request, 'user/notice/engine/_uuid.html')
# order 注文履歴
def order(request):
    return render(request, 'user/order/index.html')
def odetail(request):
    return render(request, 'user/order/_uuid.html')
def cancel(request):
    return render(request, 'user/order/cancel/index.html')
def ocdetail(request):
    return render(request, 'user/order/cancel/_uuid.html')
def onotExecuted(request):
    return render(request, 'user/order/notExecuted/index.html')
def ondetail(request):
    return render(request, 'user/order/notExecuted/_uuid.html')
# register 新規登録
def register(request):
    return render(request, 'user/register/index.html')
def rdetail(request):
    return render(request, 'user/register/_uuid.html')
# reserve 予約
def reserve(request):
    return render(request, 'user/reserve/index.html')
def rdate(request):
    return render(request, 'user/reserve/date/index.html')
def rddetail(request):
    return render(request, 'user/reserve/date/_uuid.html')
def rpayment(request):
    return render(request, 'user/reserve/payment/index.html')
def rpdetail(request):
    return render(request, 'user/reserve/payment/_uuid.html')
def rconfirmation(request):
    return render(request, 'user/reserve/confirmation/index.html')
def rdone(request):
    return render(request, 'user/reserve/done/index.html')
# search 検索
def search(request):
    return render(request, 'user/search/index.html')
# setting 設定
def setting(request):
    return render(request, 'user/setting/index.html')
def sinquiry(request):
    return render(request, 'user/setting/companyInquiry/index.html')
def scontact(request):
    return render(request, 'user/setting/contact/index.html')
# creditについては変更と追加ができないとだめだと思います
def scredit(request):
    return render(request, 'user/setting/credit/index.html')
def screditAdd(request):
    return render(request, 'user/setting/credit/creditAdd.html')
def screditEdit(request):
    return render(request, 'user/setting/credit/creditEdit.html')
def shidden(request):
    return render(request, 'user/setting/hidden/index.html')
def stpoint(request):
    return render(request, 'user/setting/tpoint/index.html')
def sunsubscribe(request):
    return render(request, 'user/setting/unsubscribe/index.html')
def suserDetailChange(request):
    return render(request, 'user/setting/userDetailChange/index.html')


# company
def company(request):
    return render(request, 'company/business/index.html')
def booking(request):
    return render(request, 'company/booking/index.html')
def bookdetail(request):
    return render(request, 'company/booking/_uuid.html')
def coupon(request):
    return render(request, 'company/business/coupon/index.html')
def player(request):
    return render(request, 'company/business/player/index.html')
def medetail(request):
    return render(request, 'company/business/player/_uuid.html')
def read(request):
    return render(request, 'company/business/read/index.html')
def redetail(request):
    return render(request, 'company/business/read/_uuid.html')
def valuation(request):
    return render(request, 'company/business/valuation/index.html')
def compilation(request):
    return render(request, 'company/compilation/index.html')
def compon(request):
    return render(request, 'company/compilation/coupon/index.html')
def complay(request):
    return render(request, 'company/compilation/player/index.html')
def cmdetail(request):
    return render(request, 'company/compilation/player/_uuid.html')
def comre(request):
    return render(request, 'company/compilation/read/index.html')
def comvalua(request):
    return render(request, 'company/compilation/valuation/index.html')
def survey(request):
    return render(request, 'company/survey/index.html')
def voice(request):
    return render(request, 'company/voice/index.html')
def vcdetail(request):
    return render(request, 'company/voice/_uuid.html')
def vedetail(request):
    return render(request, 'company/voice/engine/index.html')



# engine
def engine(request):
    return render(request, 'engine/start/index.html')
# analytics　分析
def analytics(request):
    return render(request, 'engine/analytics/index.html')
# contact　お問い合わせ
def contact(request):
    return render(request, 'engine/contact/client/index.html')
def client(request):
    return render(request, 'engine/contact/client/_uuid.html')
def inquire(request):
    return render(request, 'engine/contact/customer/index.html')
def customer(request):
    return render(request, 'engine/contact/customer/_uuid.html')
# guest　お客様
def guest(request):
    return render(request, 'engine/guest/index.html')
def gdetail(request):
    return render(request, 'engine/guest/_uuid.html')
# edit　編集
def edit(request):
    return render(request, 'engine/edit/index.html')
# manage　予約管理
def manage(request):
    return render(request, 'engine/manage/index.html')
def mdetail(request):
    return render(request, 'engine/manage/_uuid.html')
# publish　会社
def publish(request):
    return render(request, 'engine/publish/index.html')
def pdetail(request):
    return render(request, 'engine/publish/_uuid.html')
def diary(request):
    return render(request, 'engine/publish/diary/index.html')
def ddetail(request):
    return render(request, 'engine/publish/diary/_uuid.html')
def employ(request):
    return render(request, 'engine/publish/employ/index.html')
def xdetail(request):
    return render(request, 'engine/publish/employ/_uuid.html')
def menu(request):
    return render(request, 'engine/publish/menu/index.html')
def rate(request):
    return render(request, 'engine/publish/rate/index.html')
# write　記事
def write(request):
    posts = Post.objects.order_by('-published'),
    # count = posts.count('Post')
    for obj in posts:
        print(obj)
        # count = obj.count()
    contexts = ({
        'post_list' : obj,
        # 'counts' : count,
        'categories' : Category.objects.order_by('name'),
    })
    return render(request, 'engine/writer/index.html', {'contexts': contexts})
def wdetail(request, pk):
    posts = Post.objects.get(pk=pk)
    return render(request, 'engine/writer/_uuid.html', {'posts': posts})
def category(request, category_id):
    posts =  Post.objects.filter(category_id=category_id),
    for post in posts:
        print(post)
    contexts = ({
        'post_list' : post,
        'categories' : Category.objects.order_by('name'),
    })
    return render(request, 'engine/writer/category/index.html', {'contexts': contexts})
