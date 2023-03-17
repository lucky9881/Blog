from django.db import models

# Create your models here.

from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from datetime import datetime

# Create your models here.
class Apps(models.Model):
    
    Apps_titile = HTMLField()
    Apps_msg = HTMLField()
    datetime = models.DateTimeField(datetime.today())
    Apps_img = models.FileField(upload_to="Apps/",max_length=500,null=True,default=None)
    
    Apps_img1 = models.FileField(upload_to="Apps/",max_length=500,null=True,default=None,)
    Apps_img2= models.FileField(upload_to="Apps/",max_length=500,null=True,default=None)
    Apps_img3= models.FileField(upload_to="Apps/",max_length=500,null=True,default=None)
    Apps_img4 = models.FileField(upload_to="Apps/",max_length=500,null=True,default=None)
    
    Apps_links = HTMLField(null=True,default=None)
    
    
    Apps_slug = AutoSlugField(populate_from='Apps_titile',unique=True,null=True,default=None)
    
    
    
    
    def __str__(self):
        return self.Apps_titile  
    
      