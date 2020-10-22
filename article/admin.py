from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Article,Comment,proje

# Register your models here.

# admin.site.register(Comment)

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):

#     list_display = ["title","author","created_date"]

#     list_display_links = ["title","created_date"]

#     search_fields = ["title"]

#     list_filter = ["created_date"]
#     class Meta:
#         model = Article


@admin.register(proje)
class ProjeAdmin(ImportExportModelAdmin):
    #list_display=[("author")]
    list_display=["product_name","category","product_code","created_date","author"]
    #list_display_links=["product_name","category","product_code","created_date","author"]
    search_fields=["product_name"]
    list_filter=[("author",admin.RelatedOnlyFieldListFilter),"created_date"]
    list_per_page=15
    list_select_related=[("author")]

    
    class Meta:
        model=proje
