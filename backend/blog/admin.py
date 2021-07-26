from django.contrib import admin
from .models import Law, Category
# Register your models here.

class LawAdmin(admin.ModelAdmin):
    #fields = ['title', 'poster', 'description', 'slug', 'status', 'tags', 'category']
    exclude = ['created', 'author']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super(LawAdmin, self).save_model(request, obj, form, change)

admin.site.register(Law, LawAdmin)


admin.site.register(Category)
