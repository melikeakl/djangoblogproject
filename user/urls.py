from django.contrib import admin
from django.urls import path
from . import views 
app_name = 'users' 

urlpatterns = [
    path('register/', views.register, name="register"),  # Kullanıcı kayıt sayfası için URL, views.register fonksiyonunu çağırır.
    path('login/', views.loginUser, name="login"),  # Kullanıcı giriş sayfası için URL, views.login_view fonksiyonunu çağırır.
    path('logout/', views.logoutUser, name="logout"),  # Kullanıcı çıkış sayfası için URL, views.logout_view fonksiyonunu çağırır.
]
 