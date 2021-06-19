from django.urls import path, include
from .views import ProfileView, ProfileEdit
urlpatterns = [
    path('Info/', ProfileView.as_view(), name='Profile'), 
    path('<int:pk>/Edit/', ProfileEdit.as_view(), name = 'Edit')
]
