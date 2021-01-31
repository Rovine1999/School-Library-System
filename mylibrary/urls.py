from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import LibraryCreateView,LibraryListView,LibraryUpdateView,LibraryDeleteView


urlpatterns=[
    path('',LibraryListView.as_view(),name = 'index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]