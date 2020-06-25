from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
from .models import Profile
class ProfileView(ListView, LoginRequiredMixin):
    model = Profile
    template_name = "Profile/Profile_view.html"
    login_url = 'Login/login'
    def get(self, request):
        current_user = request.user
        query_set = Profile.objects.get(user=current_user)
        return render(request, self.template_name, {'Profile':query_set})
class ProfileEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "Profile/Update.html"
    fields = ('Bio', 'Profile_Image', 'Address')
    
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
    
    