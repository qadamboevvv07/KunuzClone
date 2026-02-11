from django.contrib import admin

from app.models import News, Category



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'publish_time', 'status', 'category']
    list_filter = ['title', 'category', 'publish_time']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ('-title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
