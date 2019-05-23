from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from django.views import generic
from .models import Article,Category
from django.core.exceptions import MultipleObjectsReturned

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
    articles = Article.objects.order_by('-published'),
    # count = posts.count('Post')
    for obj in articles:
        print(obj)
        # count = obj.count()
    contexts = ({
        'article_list' : obj,
        # 'counts' : count,
        'categories' : Category.objects.order_by('name'),
    })
    return render(request, 'engine/writer/index.html', {'contexts': contexts})
def wdetail(request, pk):
    articles = Article.objects.get(pk=pk)
    return render(request, 'engine/writer/_uuid.html', {'articles': articles})
def category(request, category_id):
    articles =  Article.objects.filter(category_id=category_id),
    for article in articles:
        print(article)
    contexts = ({
        'article_list' : article,
        'categories' : Category.objects.order_by('name'),
    })
    return render(request, 'engine/writer/category/index.html', {'contexts': contexts})
