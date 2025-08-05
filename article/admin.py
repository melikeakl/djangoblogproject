from django.contrib import admin

# Register your models here.

#articleı kaydetme
from .models import Article, Comment
#admin.site.register(Comment)  # Comment modelini admin paneline kaydettik.  # Comment modelini admin paneline kaydettik, bu
#admin.site.register(Article)  # Article modelini admin paneline kaydettik.
@admin.register(Article)  # Article modelini admin paneline kaydettik, bu şekilde daha okunabilir. decarator şeklinde yazdık.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date']  # Admin panelinde makalelerin başlığı, yazarı ve oluşturulma tarihi görünsün istedik.
    list_display_links = ['title']  # Başlığa tıklanabilir link olarak ayarladık, böylece başlığa tıklayınca makalenin detayına gidebiliriz.

    search_fields = ['title']  # Admin panelinde makaleleri başlık ve içerik ile arayabilmemizi sağladık.

    list_filter = ['created_date']  # Admin panelinde makaleleri oluşturulma tarihine göre filtreleyebilmemizi sağladık.
    #istersek içine author falan da yazabilirdik
    
    class Meta: #meta ismi django tarafından belirleniyor.
        model = Article # Modeli admin panelinde kullanacağımızı belirttik. django böyle bir kullanım öneriyor

admin.site.register(Comment)  # Comment modelini admin paneline kaydettik, bu şekilde admin panelinde yorumları da görebiliriz.
    