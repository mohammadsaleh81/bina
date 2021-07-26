from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.deletion import CASCADE

# Create your models here.
class Law(models.Model):
    TRUE_FALSE_CHOICES = (
    (True, 'منتشر شده'),
    (False, 'پیش نویس')
)

    title = models.CharField('عنوان', max_length=50)
    description = RichTextField('متن', )
    poster = models.ImageField('تصویر', upload_to="images")
    status =models.BooleanField('وضعیت', choices = TRUE_FALSE_CHOICES)
    created = models.DateTimeField('تاریخ انتشار', auto_now_add=True)
    author =models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    slug = models.SlugField('لینک کوتاه',)
    Category = models.ManyToManyField('Category', verbose_name='دسته بندی')
    tags = TaggableManager(verbose_name="تگ")

    class Meta:
        verbose_name = 'قانون'
        verbose_name_plural = "قانون ها"

    def __str__(self) -> str:
        return self.title




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


