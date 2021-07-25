

### ساخت مدل های پروژه: 

در فایل models.py پگیج مرد نظر میتوانیم با ایجاد یک کلاس و ارث بری از modes خود جنگو در آدرس django.db.models میتوان مدل ها را نوشت و جدول های دیتابیس را ساخت

با دستور زیر میتوانیم مدل ها را آماده برای ورود به دیتابیس کنیم 

```python
python manage.py makemigrations
```



و با دستور زیر جدول ها در دیتابیس ایجاد میشوند‍

```python
python manage.py migrate
```



### چند نکته

- برای استفاده از تصاویر در مدل ها باید پکیج pillow را با دستور نصب کرد

  ‍‍‍‍‍

  ```python
  pip install pillow
  ```

-  تنظیمات مربوط به بارگزاری media در جنگو بصورت زیر اصت

  ‍‍

  ```python
  MEDIA_URL = '/media/'
  MEDIA_DIR = os.path.join(BASE_DIR, 'media')
  
  ```

- و باید تکه کد زیر به فایل urls.py اضافه شود 

  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

   

  - تنظیمات فایل ها استاتیک باید به صورت زیر به فایل settings.py اضافه شود

    ```python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR , 'static') 
    
    ```

    

