from django.urls import path
from . import views

urlpatterns = [
    path('<str:field>/<str:lookup>/<str:search_string>/', views.employee_search, name='employee_search'),
    path('', views.default_view, name='default_view'),
]
