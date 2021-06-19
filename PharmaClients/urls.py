from django.urls import path
from .views import HomePageView, AboutView, ContactView,  SearchResultView, UserFormView, create_order_list, DrugDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutView, name = 'about'),
    path('contact/', ContactView, name = 'contact'),
    path('search/', SearchResultView.as_view(), name = 'search'),
    path('signup/', UserFormView.as_view(), name = 'signup'),
    path('DrugList/<int:pk>', DrugDetailView.as_view(), name='Detail'),
    path('Order/<int:pk>', create_order_list.as_view(), name='Order')
]
