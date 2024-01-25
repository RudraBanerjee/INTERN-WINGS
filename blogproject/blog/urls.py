from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('about',views.about,name="about"),
    path('signup',views.signup,name="signup"),
    path('submitsignup',views.submitsignup,name="submitsignup"),
    path('create_post',views.create_post,name="create_post"),
    path('post_created',views.post_created,name="post_created"),
    path('search', views.search, name='search'),
    path('Catagories',views.catagories,name='Catagories'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('account',views.account_details,name="Myaccount")
]