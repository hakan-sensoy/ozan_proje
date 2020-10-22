from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard_two/',views.dashboard_two,name = "dashboard_two"),
    path('add/',views.add,name = "add"),
    path('article/<int:id>',views.detail,name = "detail"),
    path('update_two/<int:id>',views.update,name = "update_two"),

    path('delete_two/<int:id>',views.delete,name = "delete_two"),
    path('',views.articles,name = "articles"),
    path('comment/<int:id>',views.addComment,name = "comment"),
    
]
