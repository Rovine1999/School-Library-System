from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import BooksCreateView,BooksListView,BooksUpdateView,BooksDeleteView


urlpatterns=[
    path('',views.index,name = 'index'),
    path('add/new', BooksCreateView.as_view(), name='add'),
    path('search/category', views.search_category, name = 'search_category'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('<username>/profile', views.user_profile, name='profile'),
    path('post/<int:pk>/update/',BooksUpdateView.as_view(), name="updateForm"),
    path('post/<int:pk>/delete/',BooksDeleteView.as_view(), name="deleteForm"),
]