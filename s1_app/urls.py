from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marks', views.marks, name='marks'),
    path('ranks', views.ranks, name='ranks'),
    path('name_year/<int:year>', views.name_year, name='name_year')
]