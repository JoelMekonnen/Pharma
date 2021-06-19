from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views import View 
from .forms import UserForm, OrderForm, DeliveryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login
from .models import DrugList, DrugOrder, Delivery
from django import forms
# Create your views here.
class HomePageView(View):
    model = DrugList
    template_name = 'index.html'
    def get(self, request):
        if not request.user.is_anonymous:
            OrderHistory = DrugOrder.objects.filter(Ordered_By=request.user).order_by('-Order_Date')[0:2]
            Drugs = DrugList.objects.order_by('-DateAdded')[0:3]
            isAvail = False
            if len(OrderHistory) > 0:
                isAvail = True
            return render(request, self.template_name, {'history':OrderHistory, 'DrugList':Drugs, 'display':isAvail})
        else:
            return render(request, self.template_name)
def AboutView(request):
    return render(request, 'about.html')
def ContactView(request):
    return render(request, 'contact.html')

class SearchResultView(ListView):
    model = DrugList
    template_name = 'searchResult.html'
    
    def get_queryset(self):
        query = self.request.GET.get('searchText')
        object_list = DrugList.objects.filter(Drug_name__icontains=query)
        return object_list
class UserFormView(View):
    form_class = UserForm
    template_name = 'signup.html'

    def get(self, request):
         form = UserForm
         return render(request, self.template_name, {'form':form})
    def post(self, request):
          form = UserForm(request.POST)
          if form.is_valid():
              user = form.save(commit=False)   
              #Cleaned (normalized data)
              username = form.cleaned_data['username']
              password = form.cleaned_data['password']
              user.set_password(password)
              user.save()
              
          return redirect('login')
class DrugDetailView(DetailView):
    model = DrugList
    template_name = 'snippets/DrugDetail.html'
    context_object_name = 'drugs'

class create_order_list(LoginRequiredMixin, View):
    form_class = OrderForm
    template_name = 'snippets/Order.html'

    def get(self, request, pk):
        form = OrderForm
        MyForm = DeliveryForm
        DrugInfo = DrugList.objects.get(id=pk)
        return render(request, self.template_name, {'form':form, 'price':DrugInfo.price, 'DrugInfo':DrugInfo,  'MyForm':MyForm})
    def post(self, request, pk):
        form = OrderForm(request.POST)
        myForm = DeliveryForm(request.POST)
        if myForm.is_valid:
            delivery = myForm.save(False)
            delivery.save()
        if form.is_valid():
            orders = form.save(False)
            orders.Drug_name = DrugList.objects.get(id=pk)
            orders.Ordered_By = request.user
            orders.TotalPrice =  int(form['Quantity'].value()) * int(DrugList.objects.get(id=pk).price)
            orders.Deliveries = Delivery.objects.latest('id')
            orders.save()
        
        return redirect('home')




