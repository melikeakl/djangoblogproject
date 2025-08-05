from django.shortcuts import render, redirect
from . forms import RegisterForm, LoginForm #forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):
    # Kullanıcı kayıt işlemleri burada yapılacak
    """
    form = RegisterForm()  # RegisterForm sınıfından form nesnesi oluşturur.
    context = {
        'form': form  # Form nesnesini context sözlüğüne ekler, böylece template içinde kullanılabilir.
    }
    return render(request, 'register.html', context)  # 'register.html' template dosyasını render eder ve context'i gönderir.get request
    """
    """if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): #clean metodu çağrılır ve form verileri doğrulanır
            # Form verileri geçerliyse, kullanıcı kaydı işlemleri burada yapılacak
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User(username = username) # Yeni bir User nesnesi oluşturur
            newUser.set_password(password) # Parolayı hash'ler yani düz metin olarak kaydetmez
            newUser.save()
            login(request, newUser) # Kullanıcıyı oturum açmış olarak işaretler, ilk parametre request, ikinci parametre ise yeni oluşturulan kullanıcı nesnesidir.

            return redirect("index") # Kullanıcı kaydı başarılıysa, index sayfasına yönlendirir
        
         #isvalid değilse yani else ise
        context = {
            "form": form
        }
        return render(request, "register.html", context) #buradaki amaç yukarıdaki gibi regiterform sınıfından form nesnesi oluşturduk ve bunu context sözlüğüne ekledik. Böylece template içinde form nesnesini kullanabileceğiz.
            
    else:
        form = RegisterForm() #boş form
        context = {
            "form": form
        }
        return render(request, "register.html", context) #buradaki amaç yukarıdaki gibi regiterform sınıfından form nesnesi oluşturduk ve bunu context sözlüğüne ekledik. Böylece template içinde form nesnesini kullanabileceğiz.
     """ #burası çok karışık daha kısa yolu aşağıda
    
    form = RegisterForm(request.POST or None)  # POST isteği varsa form verilerini alır, yoksa boş form oluşturur direkt olarak.
    if form.is_valid(): #clean metodu çağrılır ve form verileri doğrulanır eğer postsa bu kısma girer getse none dönecek zaten
            # Form verileri geçerliyse, kullanıcı kaydı işlemleri burada yapılacak
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User(username = username) # Yeni bir User nesnesi oluşturur
            newUser.set_password(password) # Parolayı hash'ler yani düz metin olarak kaydetmez
            newUser.save()
            login(request, newUser) # Kullanıcıyı oturum açmış olarak işaretler, ilk parametre request, ikinci parametre ise yeni oluşturulan kullanıcı nesnesidir.
            messages.success(request, "Kayıt başarılı!")  # Kullanıcıya başarılı kayıt mesajı gösterir

            
            return redirect("index") # Kullanıcı kaydı başarılıysa, index sayfasına yönlendirir
   
    context = { #else durumu yine get ise buraya döncek
            "form": form
        }
    return render(request, "register.html", context)    


    
def loginUser(request):
    # Kullanıcı giriş işlemleri burada yapılacak
    form = LoginForm(request.POST or None)  # POST isteği varsa form verilerini alır, yoksa boş form oluşturur
    context = {
        'form': form  # Form nesnesini context sözlüğüne ekler, böylece template içinde kullanılabilir.
    }

    if form.is_valid(): #postsa bu kısma girer
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username = username,password = password) # Kullanıcıyı doğrular, eğer kullanıcı adı ve parola doğruysa kullanıcı nesnesini döner, yanlışsa None döner.
        if user is None:
           messages.info (request, "Kullanıcı adı veya parola yanlış!")  # Kullanıcıya hata mesajı gösterir
           return render(request, 'login.html', context)  # Hata mesajı ile birlikte
        
        messages.success(request, "Giriş başarılı!")  # Kullanıcıya başarılı giriş mesajı gösterir

        login(request, user)  # Kullanıcıyı oturum açmış olarak işaretler.
        return redirect("index") #anasayfaya dön

    return render(request, 'login.html',context) 

def logoutUser(request):
    # Kullanıcı çıkış işlemleri burada yapılacak
    logout(request)  # Kullanıcıyı oturumdan çıkarır.
    messages.success(request, "Çıkış başarılı!")  # Kullanıcıya başarılı çıkış mesajı gösterir
    return redirect("index")  # Kullanıcıyı anasayfaya yönlendirir

