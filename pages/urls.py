from django.urls import path
from . import views



urlpatterns = [
    path('main/', views.main, name='main'),
    path('main/login/home/', views.home, name='home'),
    path('main/AddStudent/', views.AddStudent, name='AddStudent'),
    path('main/UpdateInfo/', views.UpdateInfo, name='UpdateInfo'),
    path('main/View/', views.View, name='View'),
    path('main/Search/', views.Search, name='Search'),
    path('main/Search/', views.search, name='search'),
    path('main/login/', views.login, name='login'),
    path('main/UpdateInfo/<int:id>', views.delete, name='delete'),
    path('<int:id>', views.update, name='update'),
    # path('main/update/updaterecord<int:id>',
        #  views.updaterecord, name='updaterecord'),sssss
]