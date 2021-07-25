from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Law(models.Model):
    TRUE_FALSE_CHOICES = (
    (True, 'منتشر شده'),
    (False, 'پیش نویس')
)

    title = models.CharField('عنوان', max_length=50)
    description = RichTextField('متن')
    poster = models.ImageField('تصویر', upload_to="images")
    status =models.BooleanField('وضعیت', choices = TRUE_FALSE_CHOICES)
    created = models.DateTimeField('تاریخ انتشار', auto_now_add=True)
    author =models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    slug = models.SlugField('لینک کوتاه')

    class Meta:
        verbose_name = 'قانون'
        verbose_name_plural = "قانون ها"

    def __str__(self) -> str:
        return self.title

