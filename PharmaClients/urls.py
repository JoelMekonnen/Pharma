from django.urls import path
from .views import HomePageView, AboutView, ContactView, LoginView, SearchResultView

urlpatterns = [
    path('', HomePageView, name = 'home'),
    path('about/', AboutView, name = 'about'),
    path('contact/', ContactView, name = 'contact'),
    path('login/', LoginView, name = 'login'),
    path('search/', SearchResultView.as_view(), name = 'search')
]
