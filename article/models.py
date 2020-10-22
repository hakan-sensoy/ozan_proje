from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

class proje(models.Model):
    category_box = (
        ('Arts, Crafts & Sewing','Arts, Crafts & Sewing'),
        ('Automotive','Automotive'),
        ('Baby Products','Baby Products'),
        ('Beauty & Personal Care','Beauty & Personal Care'),
        ('Books','Books'),
        ('Cell Phones & Accessories','Cell Phones & Accessories'),
        ('Clothing, Shoes & Jewelry','Clothing, Shoes & Jewelry'),
        ('Collectibles & Fine Art','Collectibles & Fine Art'),
        ('Electronics','Electronics'),
        ('Grocery & Gourmet Food','Grocery & Gourmet Food'),
        ('Health & Household','Health & Household'),
        ('Home & Kitchen','Home & Kitchen'),
        ('Industrial & Scientific','Industrial & Scientific'),
        ('Movies & TV','Movies & TV'),
        ('Patio, Lawn & Garden','Patio, Lawn & Garden'),
        ('Pet Supplies','Pet Supplies'),
        ('Software','Software'),
        ('Sports & Outdoors','Sports & Outdoors'),
        ('Tools & Home Improvement','Tools & Home Improvement'),
        ('Toys & Games','Toys & Games'),
        ('Video Games','Video Games'),
        
    )
    product_type_box=(
        ('Individual','Individual'),
        ('Bundle','Bundle'),
        ('Glass','Glass'),
        ('Hazardous','Hazardous'),
        ('Order Fulfillment','Order Fulfillment')
    )

    location_box=(
        ('URM1','URI Prep & Ship - Montgomery,AL'),
    )

    sales_channel_box=(
        ('Amazon','Amazon'),
        ('eBay','eBay'),
    )
    author=models.ForeignKey("auth.user",on_delete=models.PROTECT)
    product_name=models.CharField(max_length=50,null=False,blank=True)
    category = models.CharField(max_length=25, choices=category_box,null=False,blank=True)
    product_code=models.IntegerField(verbose_name="Asin or upc *",null=False,blank=False)
    product_type = models.CharField(max_length=25, choices=product_type_box,null=False,blank=True)
    sku=models.CharField(max_length=30, verbose_name="Sku (if empty, automatically generated)",null=False,blank=True)
    quantity=models.CharField(max_length=30,verbose_name="Quantity *",null=False,blank=False)
    location_box = models.CharField(max_length=25,default=location_box[0][0] ,choices=location_box,null=False,blank=True)
    sales_channel = models.CharField(max_length=25, choices=sales_channel_box,null=False,blank=True)

    created_date=models.DateTimeField(auto_now_add=True,null=False,blank=True)




def __str__(self):
        return self.product_name       