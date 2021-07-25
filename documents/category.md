### اضافه کردن مدل دسته بندی

برای دسته بندی پروژه یک مدل جدید بصورت زیر ایجاد میکنیم

‍‍

```python
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="والد")
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=100, verbose_name="آدرس دسته‌بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی ها"
        ordering = ['parent__id', 'position']
```



این مدل یک کلید خارجی به خودش دارد که به واسطه آن میتوانیم دسته بندی های والد ایجاد کنیم

و در مدل مقاله فیلدی با عنوان دسته بندی ایجاد میکنیم که بتوانیم برای مقالاتمان دسته بندی ایجاد کنیم