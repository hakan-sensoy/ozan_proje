from django import forms
from .models import Article,proje
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]


class projeForm(forms.ModelForm):
    class Meta:
        model = proje
        fields = ["product_name","category","product_code","product_type","sku","quantity","location_box","sales_channel"]
        widgets={
            'product_code':forms.Textarea(attrs={'cols':10,'rows':1}),
            'quantity':forms.Textarea(attrs={'cols':10,'rows':1}),
            
        }