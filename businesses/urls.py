from django.urls import path
from .views import add_business, business_list, business_detail

urlpatterns = [
    path('', business_list, name='business_list'),
    path('add/', add_business, name='add_business'),
    path('<int:pk>/', business_detail, name='business_detail'),
]

