"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from article import views

app_name = 'blog'  # Uygulama adını belirtir, böylece URL'ler uygulama içinde tanımlanabilir.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= "index"),  # Admin paneline yönlendirme, böylece ana sayfada admin paneli açılacak.
    #name=index yazma sebebim, url'yi daha sonra kullanabilmek için. Böylece url'yi değiştirdiğimizde, kodlarımızı değiştirmemize gerek kalmaz.
    path('about/', views.about, name= "about"),
    #path('detail/<int:id>/', views.detail, name="detail"),  # Detay sayfası için dinamik URL, id parametresi ile makale detayını gösterir.
    # <int:id> kısmı, URL'de gelen id parametresini integer olarak alır ve views.detail fonksiyonuna gönderir.
    # views.detail fonksiyonunda bu id parametresini kullanarak makale detayını alabiliriz.
    path('articles/', include('article.urls')),  # article uygulamasının URL'lerini dahil eder, böylece article.urls içindeki URL'ler kullanılabilir.
    path('user/', include('user.urls')),  # user uygulamasının URL'lerini dahil eder, böylece user.urls içindeki URL'ler kullanılabilir.
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Media dosyalarını statik olarak sunar, böylece kullanıcılar yüklenen medya dosyalarına erişebilir.


