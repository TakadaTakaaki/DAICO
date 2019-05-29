from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from app.models import Article,Category
from django.core.exceptions import MultipleObjectsReturned
from app.models import Company_data,Plan,Staff
from django.shortcuts import redirect
from .forms import Company_dataAdd


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('company')
    template_name = 'client/signup.html'

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
    company_datas = Company_data.objects.order_by('name')
    return render(request, 'company/compilation/index.html', {'company_datas' : company_datas})
def hensyu(request, users__user_type):
    company_datas = Company_data.objects.filter(users__user_type="A")
    # users = User.objects.filter(pk=company_data_id),
    if (request.method == 'POST'):
        obj = Company_data()
        info = Company_dataAdd(request.POST,instance=obj)
        info.save()
        return redirect(to='/compilation')
    modelform_dict = {
        'title': '編集ページ',
        'form': Company_dataAdd(),
    }
    return render(request, 'company/compilation/_uuid.html', modelform_dict)
def compon(request):
    plans = Plan.objects.order_by('genre')
    return render(request, 'company/compilation/coupon/index.html', {'plans' : plans})
def complay(request):
    staffs = Staff.objects.order_by('name')
    return render(request, 'company/compilation/player/index.html', {'staffs' : staffs})
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