from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label='Kullanıcı Adı')
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Parola')
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Parolayı Onayla')
    
    def clean(self): #clean metodu, form verilerini doğrulamak için kullanılır.
        username = self.cleaned_data.get('username') # Kullanıcı adını alır
        password = self.cleaned_data.get('password') # Parolayı alır
        confirm = self.cleaned_data.get('confirm') # Parolayı onaylar

        if password and confirm and password != confirm: #parola alani ve confirm alanı doldurulmuş mu ve password eşit değişle confirme
            raise forms.ValidationError("Parolalar eşleşmiyor!") #raise ValidationError, eDjango’nun form doğrulama sistemi içinde, kullanıcı yanlış veri girdiğinde hata fırlatmak için kullanılır.
        
        values = { #sözlük yapısıyla döndürmemiz lazım username ve passwordu, else durumu
            'username': username,
            'password': password,
        }

        return values #values sözlüğünü döndürür, böylece form verileri temizlenmiş ve doğrulanmış olur.

class LoginForm(forms.Form):
    username = forms.CharField(label='Kullanıcı Adı')
    password = forms.CharField(widget=forms.PasswordInput, label='Parola')
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if not username or not password:
            raise forms.ValidationError("Kullanıcı adı ve parola boş bırakılamaz!")

        return self.cleaned_data  # Temizlenmiş verileri döndürür

   