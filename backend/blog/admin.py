from django.apps.registry import apps
from django.contrib import admin
from .models import Law, Category
from taggit.models import Tag
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.admin import AdminSite
import blog
from django.contrib import auth


class MyAdminSite(AdminSite):
    
    site_header = "مدیریت سامانه بینا"
    site_title  = "مدیریت سامانه بینا"
    index_title = "مدیریت سامانه بینا"
 
    
# Creating a sort function
    def get_app_list(self, request):
        app_list = super(MyAdminSite, self).get_app_list(request)
        temp = app_list.pop(0)
        app_list.append(temp)
        print(app_list)
        app_dict = self._build_app_dict(request) 
 
    
        return app_list
   
#hidden app in admin panel
admin.site.unregister(Tag)



# Register your models here.

class LawAdmin(admin.ModelAdmin):
    exclude = ['created', 'author']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super(LawAdmin, self).save_model(request, obj, form, change)

site = MyAdminSite()
site.register(Law, LawAdmin)
site.register(Category)
site.register(Group, GroupAdmin)
site.register(User, UserAdmin) 



