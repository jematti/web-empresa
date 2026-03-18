from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('published', )
    search_fields = ('title', 'content','author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'category__name')


    def post_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all().order_by('name')])
    post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)    