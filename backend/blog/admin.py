from django.contrib import admin
from .models import Law
# Register your models here.

class LawAdmin(admin.ModelAdmin):
    fields = ['title', 'poster', 'description', 'slug', 'status']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super(LawAdmin, self).save_model(request, obj, form, change)

admin.site.register(Law, LawAdmin)
