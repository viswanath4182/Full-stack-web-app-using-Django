from django.urls import path
from .views import home, marks, ranks, name_year, register, addUser

urlpatterns = [
    path('', home, name='home'),
    path('marks', marks, name='marks'),
    path('ranks', ranks, name='ranks'),
    path('name_year/<int:year>', name_year, name='name_year'),
    path('register', register, name='register'),
    path('addUser', addUser, name='addUser')

]