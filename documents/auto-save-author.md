### ذخیره خودکار نویسنده

​	با استفاده از تابع save_model در فایل admin.py میتوانیم این عملیات را به نحو زیر انجام دهیم 

‍

```python

class LawAdmin(admin.ModelAdmin):
    fields = ['title', 'poster', 'description', 'slug', 'status']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super(LawAdmin, self).save_model(request, obj, form, change)

admin.site.register(Law, LawAdmin)
```



