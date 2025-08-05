from django.contrib import admin
from django.urls import path
from . import views # article uygulamasının views modülünden views fonksiyonlarını içe aktarır.
app_name = 'article' # Uygulama adını belirtir, böylece URL'ler uygulama içinde tanımlanabilir.

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"), # Dashboard sayfası için URL, views.dashboard fonksiyonunu çağırır.
    path('addarticle/', views.addarticle, name="addarticle"),
    path('article/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),  # Makale silme işlemi için URL, views.delete fonksiyonunu çağırır.
    path('', views.articles, name="articles"),  # Ana sayfa için URL, views.articles fonksiyonunu çağırır. 
    path('comment/<int:id>', views.addComment, name="comment"),  # Yorum ekleme işlemi için URL, views.comment fonksiyonunu çağırır.
]    