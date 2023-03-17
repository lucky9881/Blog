from django.shortcuts import render
from home.models import Contact
from datetime import datetime
from blogs.models import Blog
from apps.models import Apps

# Create your views here.
def index(requeast):
    blogs =Blog.objects.all().order_by('-id') [0:4]
    appss =Apps.objects.all().order_by('-id') [0:4]
    data = {
        'blogs':blogs,
        'apps':appss
    }
    
    
    
    return render(requeast, 'index.html',data)


def about(request):
    return render(request, 'about.html')


def blog_item(request,slug):
    blogsss =Blog.objects.get(Blog_slug=slug)
    print(slug)
    data = {
        'blogdata':blogsss
    }
    return render(request, 'blog-item.html',data)


def blog(request):
    
    blogs =Blog.objects.all().order_by('-id')
    data = {
        'blogs':blogs
    }
    
    return render(request, 'blog.html',data)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        all =Contact(name=name,email=gmail,phone=phone,msg=msg,date=datetime.today())
        all.save()
    
    
    return render(request, 'contact.html')
    
    
def apps(request):
    
    appss =Apps.objects.all().order_by('-id')
    data = {
        'app':appss
    }
    
    return render(request, 'apps.html',data)

def apps_item(request,slug):
    blogsss =Apps.objects.get(Apps_slug=slug)
    print(slug)
    data = {
        'Appsdata':blogsss
    }
    return render(request, 'apps-item.html',data)
 
         

