from django.urls import path
from .views import HomePageView, AboutView, ContactView,  SearchResultView, UserFormView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutView, name = 'about'),
    path('contact/', ContactView, name = 'contact'),
    path('search/', SearchResultView.as_view(), name = 'search'),
    path('signup/', UserFormView.as_view(), name = 'signup'),
]
