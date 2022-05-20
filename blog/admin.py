from django.contrib import admin
from .models import Category, Post,Comment,Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created_at', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'created', 'post')
    list_filter = ('fname', 'lname', 'email', 'created')

admin.site.register(Category)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'created')
    list_filter = ('fname', 'lname', 'email', 'created')