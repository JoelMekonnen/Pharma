from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views import View
from .models import DrugList
# Create your views here.
def HomePageView(request):
    return render(request, 'index.html')
def AboutView(request):
    return render(request, 'about.html')
def ContactView(request):
    return render(request, 'contact.html')
def LoginView(request):
    return render(request, 'login.html')

class SearchResultView(ListView):
    model = DrugList
    template_name = 'searchResult.html'
    
    def get_queryset(self):
        query = self.request.GET.get('searchText')
        object_list = DrugList.objects.filter(Drug_name__icontains=query)
        return object_list
