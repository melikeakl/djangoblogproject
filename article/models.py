from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model): 
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name="Yazar") #user tablosunu işaret ediyor, sondaki on_delete parametresi ile silindiğinde ne olacağını belirliyoruz yani kullanıcı silinince makalede silinsin dedik casdacade ile.
    title = models.CharField(max_length=50, verbose_name="Başlık") #makale başlığı, charfield ile karakter sınırlaması koyduk.
    content = RichTextField() #makale içeriği, textfield ile sınırsız karakter yazılabilir.
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi ") #makale oluşturulma tarihi, otomatik olarak eklenir. auto_now_add ile makale ilk oluşturulduğunda tarih eklenir.
    article_image = models.FileField(blank = True, null = True, verbose_name="Makale Resmi") #makale resmi, filefield ile dosya yüklenebilir. blank ve null ile boş bırakılabilir.
    def __str__(self):
        return self.title  # Makalenin başlığını döndürür, böylece admin panelinde makale başlığı görünecektir.
    #return self.author yazsaydık da yazar bilgisi dönerdi ve articleobject yerine bu yazardı 
    
    class Meta:  # Meta sınıfı, modelin meta verilerini tanımlar.
        ordering = ['-created_date'] #başına eksi eklersek en son yazılan yorum ilk gösterilir

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments") #makale ile ilişkilendirildi, makale silinirse yorum da silinir. 
    comment_author = models.CharField(max_length=50, verbose_name="İsim") #yorum yapan kişinin adı
    comment_content = models.CharField(max_length=200, verbose_name="Yorum") #yorum içeriği
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Yorum Tarihi") #y
    def __str__(self):
        return self.comment_content  # Yorum içeriğini döndürür, böylece admin panelinde yorum içeriği görünecektir.
    
    class Meta:  # Meta sınıfı, modelin meta verilerini tanımlar.
        ordering = ['-comment_date']