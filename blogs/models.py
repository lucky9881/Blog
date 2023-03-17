from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    
    Blog_titile = HTMLField()
    Blog_msg = HTMLField()
    datetime = models.DateTimeField(datetime.today())
    Blog_img = models.FileField(upload_to="Blog/",max_length=500,null=True,default=None)
    
    Blog_img1 = models.FileField(upload_to="Blog/",max_length=500,null=True,default=None)
    Blog_img2= models.FileField(upload_to="Blog/",max_length=500,null=True,default=None)
    Blog_img3= models.FileField(upload_to="Blog/",max_length=500,null=True,default=None)
    Blog_img4 = models.FileField(upload_to="Blog/",max_length=500,null=True,default=None)
    
    Blog_slug = AutoSlugField(populate_from='Blog_titile',unique=True,null=True,default=None)
    
    
    
    
    def __str__(self):
        return self.Blog_titile  
    
      