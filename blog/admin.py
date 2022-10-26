from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content', 'categories__name')
    list_display = ('title', 'public', 'created_at')
    list_filter = ('public', 'categories__name')



# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)