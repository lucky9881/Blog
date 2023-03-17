from django.contrib import admin
from apps.models import Apps
# Register your models here.

class AppsAdmin(admin.ModelAdmin):
    list_display=('Apps_titile','datetime')
    
admin.site.register(Apps,AppsAdmin)    