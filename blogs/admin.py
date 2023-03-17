from django.contrib import admin
from blogs.models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=('Blog_titile','datetime')
    
admin.site.register(Blog,BlogAdmin)    