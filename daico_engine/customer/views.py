from django.urls import reverse_lazy
from django.views import generic
from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from app.models import Article,Category,Company_data,Genre
from django.core.exceptions import MultipleObjectsReturned
from .forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
import re
from django.db.models import Q
from django.urls import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from django.shortcuts import redirect, get_object_or_404



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

# user
def index(request):
    articles = Article.objects.order_by('-published')
    for obj in company_datas:
        print(obj)
    contexts = ({
        'company_data_list' : obj,
        # 'counts' : count,
        'genres' : Genre.objects.order_by('name'),
    })
    return render(request, 'user/home/index.html', {'articles': articles}, {'contexts': contexts})

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
    # data = get_object_or_404(Company_data, pk=pk)
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
    company_datas = Company_data.objects.order_by('name')
    return render(request, 'user/search/index.html', {'company_datas' : company_datas})
def genre(request, genre_id):
    company_datas =  Company_data.objects.filter(genre_id=genre_id),
    for company_data in company_data:
        print(company_data)
    contexts = ({
        'company_data_list' : company_data,
        'genre' : genre.objects.order_by('name'),
    })
    return render(request, 'user/search/genre/index.html', {'contexts': contexts})
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


class Company_dataListView(PaginationMixin, generic.ListView):
    template_name = "user/search/index.html"
    model = Company_data
    # success_url = reverse_lazy('search')
    
    #Serch
    def get_queryset(self):
        result = super(Company_dataListView, self).get_queryset()
        query = self.request.GET.get('q')

        if query:
            result = Company_data.objects.filter(Q(name__icontains=query, place1__icontains=query, place2__icontains=query))
            return result
        # return reverse_lazy('user/search/index.html')
# def normalize_query(query_string,
#                     findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
#                     normspace=re.compile(r'\s{2,}').sub):
#     ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
#         and grouping quoted words together.
#         Example:

#         >>> normalize_query('  some random  words "with   quotes  " and   spaces')
#         ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

#     '''
#     return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

# def get_query(query_string, search_fields):
#     ''' Returns a query, that is a combination of Q objects. That combination
#         aims to search keywords within a model by testing the given search fields.

#     '''
#     query = None # Query to search for every search term        
#     terms = normalize_query(query_string)
#     for term in terms:
#         or_query = None # Query to search for a given term in each field
#         for field_name in search_fields:
#             q = Q(**{"%s__icontains" % field_name: term})
#             if or_query is None:
#                 or_query = q
#             else:
#                 or_query = or_query | q
#         if query is None:
#             query = or_query
#         else:
#             query = query & or_query
#     return query

# def search(request):
#     query_string = ''
#     found_entries = None
#     if ('q' in request.GET) and request.GET['q'].strip():
#         query_string = request.GET['q']

#         entry_query = get_query(query_string, ['title', 'body',])

#         found_entries = Entry.objects.filter(entry_query).order_by('-pub_date')

#     return reverse_lazy('user/search/index.html',
#                           { 'query_string': query_string, 'found_entries': found_entries },
#                           context_instance=RequestContext(request))




