from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.HomePage.as_view(), name='home'),
    path('contact/', views.ContanctView.as_view(), name='contact'),
    path('success/', views.SuccessView.as_view(), name='success'),
]