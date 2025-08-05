from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse  # render fonksiyonunu kullanarak HTML dosyalarını render eder.
from .forms import ArticleForm #şuanki forms.py dosyasından ArticleForm sınıfını içe aktarır.
from django.contrib import messages # mesajları kullanmak için içe aktarır. (opsiyonel)
from .models import Article, Comment  # Article modelini içe aktarır. Bu model, veritabanındaki makaleleri temsil eder.
from django.contrib.auth.decorators import login_required # login_required decoratorunu içe aktarır.

def index(request):
    #return HttpResponse("Merhaba Django")  # Bu fonksiyon, ana sayfada "Merhaba Django" mesajını gösterir.
    # Eğer bir template kullanmak istersek, render fonksiyonunu kullanabiliriz:
    return render(request, 'index.html')  # index.html dosyasını templates klasöründe arar. ve ordakini

def about(request):
    #return HttpResponse("Hakkımızda")  # Bu fonksiyon, hakkımızda sayfasında "Hakkımızda" mesajını gösterir.
    return render(request, 'about.html')  # about.html dosyasını templates klasöründe arar. ve ordakini 

def articles(request):
    keyword = request.GET.get("keyword")  # GET isteği ile gelen "keyword" parametresini alır. Eğer yoksa None döner.
    if keyword: # Eğer keyword parametresi varsa eğer arama yapıldıysa 
        articles = Article.objects.filter(title__contains=keyword)  # Veritabanında title alanında keyworda yazılı olan makaleleri alır.
        return render(request, "articles.html", {"articles": articles})  # articles.html dosyasını templates klasöründe arar ve ordakini gösterir. 
    articles = Article.objects.all()  # Veritabanındaki tüm makaleleri alır.
    
    return render(request, 'articles.html', {"articles":articles})  # articles.html dosyasını templates klasöründe arar ve ordakini gösterir.
    

@login_required(login_url="user:login")  # Bu decorator, bu fonksiyonun sadece oturum açmış kullanıcılar tarafından erişilebilmesini sağlar.
def dashboard(request):
    articles = Article.objects.filter(author=request.user)  # Oturum açmış kullanıcının makalelerini alır.
    context = {
        "articles": articles  # context sözlüğüne makaleleri ekler.
    }
    return render(request, 'dashboard.html', context)  # dashboard.html dosyasını templates klasöründe arar ve ordakini gösterir.

@login_required(login_url="user:login")  # Bu decorator, bu fonksiyonun sadece oturum açmış kullanıcılar tarafından erişilebilmesini sağlar.
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)  # ArticleForm sınıfından form nesnesi oluşturur. Eğer POST isteği varsa, form verilerini alır.
    if form.is_valid():  # Formun geçerli olup olmadığını kontrol eder.
        #form.save()  # Form verilerini kaydeder. Oto kaydetme
        #form.save article objesini oluşturuyor sonra save yapıyor ama biz article yaptıktan sonra saveden önce bir auother bilgisi vermek zorundayız
        article = form.save(commit=False)  # Form verilerini kaydetmeden önce Article nesnesi oluşturur. Kaydetmeyi biz yapacağız Böylece sıkıntı yaşamayız
        article.author = request.user  # Article nesnesinin author alanını, oturum açmış kullanıcıya atar.
        article.save()  # Article nesnesini kaydeder. 
        messages.success(request, "Makale Başarıyla Eklendi")  # Başarılı bir şekilde makale eklendiğinde mesaj gösterir.
        return redirect("article:dashboard")  # Article uygulamasının dashboard sayfasına yönlendirir. app_name ile tanımladığımız için article:dashboard şeklinde yazıyoruz.
    

    return render(request, 'addarticle.html', {"form":form})  # addarticle.html dosyasını templates klasöründe arar ve ordakini gösterir.

def detail(request, id): #dinamik url parametresi
    #article = Article.objects.filter(id=id).first()  # Veritabanından id'si verilen makaleyi alır. first ekledik gördüğü ilk articlı göstersin diye
    article = get_object_or_404(Article, id=id)  # Veritabanından id'si verilen makaleyi alır. Eğer makale bulunamazsa 404 sayfası gösterir. Model ve sorgu giricek parantez içine
    comments = article.comments.all()  # İlgili makalenin yorumlarını alır. modeldeki related_name ile ilişkilendirilmiş yorumları alır.

    return render(request, 'detail.html', {"article":article, "comments":comments})  # detail.html dosyasını templates klasöründe arar ve ordakini gösterir.

@login_required(login_url="user:login")  # Bu decorator, bu fonksiyonun sadece oturum açmış kullanıcılar tarafından erişilebilmesini sağlar.
def update(request, id):
    article = get_object_or_404(Article, id=id)  # Veritabanından id'si verilen makaleyi alır. Eğer makale bulunamazsa 404 sayfası gösterir.
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)  # ArticleForm sınıfından form nesnesi oluşturur. Eğer POST isteği varsa, form verilerini alır. instance ile tüm bilgiler form'a göndeririz.
    if form.is_valid():  # Formun geçerli olup olmadığını kontrol eder.
        article = form.save(commit=False) # Form verilerini kaydetmeden önce Article nesnesi oluşturur. Kaydetmeyi biz yapacağız Böylece sıkıntı yaşamayız
        article.author = request.user # Article nesnesinin author alanını, oturum açmış kullanıcıya atar.
        article.save()

        messages.success(request, "Makale Başarıyla Güncellendi")  # Başarılı bir şekilde makale eklendiğinde mesaj gösterir.
        return redirect("index")
    
    return render(request, 'update.html', {"form":form})  # update.html dosyasını templates klasöründe arar ve ordakini gösterir.

@login_required(login_url="user:login") 
def delete(request, id):
    article = get_object_or_404(Article, id=id)  # Veritabanından id'si verilen makaleyi alır. Eğer makale bulunamazsa 404 sayfası gösterir.

    article.delete()  # Article nesnesini siler.
    messages.success(request, "Makale Başarıyla Silindi")  # Başarılı bir şekilde makale silindiğinde mesaj gösterir.
    return redirect("article:dashboard")  # Article uygulamasının dashboard sayfasına yönlendirir. app_name ile tanımladığımız için article:dashboard şeklinde yazıyoruz.


def addComment(request, id):
    #ilk önce post almamız gerek
    article = get_object_or_404(Article, id=id)  # Veritabanından id'si verilen makaleyi alır. Eğer makale bulunamazsa 404 sayfası gösterir.
    if request.method == "POST":  # Eğer istek POST ise
        comment_author = request.POST.get("comment_author")  # POST isteğinden "comment_author" parametresini alır.
        comment_content = request.POST.get("comment_content")  # POST isteğinden "comment_content" parametresini alır.
        
        #bir makaleye ait yeni bir yorum (Comment) nesnesi oluşturmak ve veritabanına kaydetmektir.
        newComment = Comment(comment_author=comment_author, comment_content=comment_content)  # Yeni bir Comment nesnesi oluşturur.
        newComment.article = article  # Yeni Comment nesnesinin article alanını, alınan makaleye atar.
        newComment.save()  # Yeni Comment nesnesini kaydeder.

    # return redirect("/articles/article" + str(id)) # Yorum eklendikten sonra, makalenin detay sayfasına yönlendirir. URL'yi dinamik olarak oluşturur.
    return redirect(reverse("article:detail", kwargs={"id": id}))  # Yorum eklendikten sonra, makalenin detay sayfasına yönlendirir. reverse ile URL'yi dinamik olarak oluşturur. articles/detail/15
