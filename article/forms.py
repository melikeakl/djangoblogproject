from django.forms import ModelForm
from .models import Article

# Create the form class.
class ArticleForm(ModelForm): #modelde oluşturduğumuz formları kullandık
    class Meta:
         model = Article # Article modelini kullanır. bağlantılı hale getirir
         # Formda hangi alanların yer alacağını belirtir.
         fields = ["title", "content", "article_image"] #author zaten direkt kullanıcı adı yazılacak diye eklemedik ve date de oto eklenecek diye eklemedik

