from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    
    path('',views.index,name='HOME'),
    path('index',views.index,name="Home"),
    path('home',views.index,name='HOME'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='Blog'),
    path('blog_item/<slug>',views.blog_item,name='Blog_items'),
    path('apps',views.apps,name='apps'),
    path('apps_item/<slug>',views.apps_item,name='Apps_Item'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)