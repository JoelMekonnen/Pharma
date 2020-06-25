from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views import View 
from .forms import UserForm
from django.contrib.auth import authenticate, login
from .models import DrugList
# Create your views here.
class HomePageView(ListView):
    model = DrugList
    template_name = 'index.html'
    queryset = DrugList.objects.order_by('-DateAdded')[0:3]
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
