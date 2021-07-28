from django.db import models
from django.db.models.fields import json
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE

# Create your models here.
class Law(models.Model):
    TRUE_FALSE_CHOICES = (
    (True, 'منتشر شده'),
    (False, 'پیش نویس')
)

    title = models.CharField('عنوان', max_length=50)
    #description = RichTextField('متن', )
    description = RichTextUploadingField('متن', )
    poster = models.ImageField('تصویر', upload_to="images")
    status =models.BooleanField('وضعیت', choices = TRUE_FALSE_CHOICES)
    created = models.DateTimeField('تاریخ انتشار', auto_now_add=True)
    author =models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    slug = models.SlugField('لینک کوتاه',)
    category = models.ManyToManyField('Category', verbose_name='دسته بندی')
    tags = TaggableManager(verbose_name="تگ")

    class Meta:
        verbose_name = 'قانون'
        verbose_name_plural = "قانون ها"

    def __str__(self) -> str:
        return self.title

    
    def get_cat_list(self):
        k = self.category
        breadcrumb = ['u']
        while k is not None:
            print(1)
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:1])
        return breadcrumb[-1:0:-1]



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


    def clean(self):
        k = self.parent
        while k is not None:
            if k.pk == self.pk: 
                k = k.parent
                raise ValidationError(
                {'parent': "به عنوان والد خود دسته بندی را وارد کرده اید"})

        


    def __str__(self) -> str:
        full_path = [self.title]

        k = self.parent
        while k is not None:
        
            full_path.append(k.title)
            k = k.parent
            
        return ' ->'.join(full_path[::-1])


