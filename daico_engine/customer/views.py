from django.urls import reverse_lazy
from django.views import generic
from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from app.models import Article,Category, Chat
from django.core.exceptions import MultipleObjectsReturned
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from app.models import User
from django import forms
from django.shortcuts import render_to_response
from .forms import ContactForm
from django.template import RequestContext
from django.views.generic import FormView

class Index(generic.TemplateView):
    template_name = 'user/home/index.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'user/login/index.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'user/home/index.html'


# class UserDeleteView(generic.DeleteView):
#     form_class = UserDeleteForm
#     template_name = "user/setting/unsubscribe/index.html"
#     success_url = reverse_lazy("/")
#     slug_field = 'username'
#     slug_url_kwarg = 'username'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('register')
    template_name = 'user/register/_uuid.html'

class UserChangeView(generic.UpdateView):
    model = User
    form_class = UserChangeForm
    success_url = reverse_lazy('setting')
    template_name = 'user/setting/userDetailChange/index.html'

# class PasswordChange(PasswordChangeView):
#     form_class = UserChangeForm
#     template_name = 'user/setting/userDetailChange/index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('setting')
    template_name = 'user/setting/contact/index.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# user
def index(request):
    articles = Article.objects.order_by('-published')
    return render(request, 'user/home/index.html', {'articles': articles})

# _uuidで詳細はできると思ったのでファイル名_uuid.htmlにしました

# article 記事
def article(request):
    articles = Article.objects.order_by('-published'),
    for obj in articles:
        print(obj)
    contexts = ({
        'article_list' : obj,
        'categories' : Category.objects.order_by('name'),
    })
    return render(request, 'user/article/index.html', {'contexts': contexts})
def adetail(request, pk):
    articles = Article.objects.get(pk=pk)
    return render(request, 'user/article/_uuid.html', {'articles': articles})
def type(request, category_id):
    articles =  Article.objects.filter(category_id=category_id),
    for article in articles:
        print(article)
    contexts = ({
        'article_list' : article,
        'categories' : Category.objects.order_by('name'),
    })
    return render(request, 'user/article/type/index.html', {'contexts': contexts})
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
def fav(request):
    return render(request, 'user/favorite/index.html')
# notice 通知
def notice_c(request):
    return render(request, 'user/notice/company/index.html')
def ncdetail(request):
    return render(request, 'user/notice/company/_uuid.html')
def nengine(request):
    chats = Chat.objects.order_by('-id')
    return render(request, 'user/notice/engine/index.html', {'chats': chats})
def nedetail(request, pk):
    chats = Chat.objects.get(pk=pk)
    return render(request, 'user/notice/engine/_uuid.html', {'chats': chats})
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
# def scontact(request):
#     if request.method == 'POST':
#         contacts = ContactForm(request.POST)
#     else:
#         contacts = ContactForm()
#     return render(request,'user/setting/contact/index.html',{'contacts': contacts} )
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
def suserDetailChange(request, pk):
    users = User.objects.get(pk=pk)
    return render(request, 'user/setting/userDetailChange/index.html', {'users': users})
def uuiuserDetailChange(request):
    return render(request, 'user/setting/userDetailChange/_uuid.html')