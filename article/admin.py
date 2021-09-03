from django.contrib import admin

from .models import Article, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['titel','author','created_date']
    list_display_links = ['titel','created_date']
    search_fields =['titel']
    list_filter = ['created_date']

    class Meta:
        model = Article 
