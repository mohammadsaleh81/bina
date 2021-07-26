### بخش جستجو و فیلتر 

در این بخش با استفاده از پکیج django-filters ویژگی فیلتر کردن به مقاله ها اضافه شد برای استفاده از این قابلیت باید کدهای زیر به فایل settings.py اضافه شود 

~~~python
INSTALLED_APPS = [
'django_filters'
```
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',
    ]
   
~~~

با اضافه کردن این بخش به متغیر filterset_fields در فایل views.py  دسترسی پیدا میکنیم که میتوان فیلد های قابل جستجو را در آن وارد کرد مانند تکه کد زیر

```python
filterset_fields = ["status", "author"]
```



 برای دسترسی به فیلترها در url پارامتر ها به صورت زیر است

```
http://127.0.0.1:8000/Law/?status=sample&author=sample
```



برای اضافه کردن بخش جستجو باید تکه کد زیر در فایل srttings.py در بخش REST_FRAMEWORK اضافه شود

```python
'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        ]
```

با اضافه کردن این بخش به متغیر search_fields در فایل views.py  دسترسی پیدا میکنیم که میتوان فیلد های قابل جستجو را در آن وارد کرد مانند تکه کد زیر

```python
search_fields = [
        'title',
        'description'
    ]
```

دسترسی به این بخش از قسمت url ها بصورت پارمتر مانند آدرس زیر است

```
http://127.0.0.1:8000/Law/?search=sample
```



برای اضافه کردن بخش مرتب سازی باید  تکه کد زیر در فایل srttings.py در بخش REST_FRAMEWORK اضافه شود

```python
'DEFAULT_FILTER_BACKENDS': [
	'rest_framework.filters.OrderingFilter',
]
```

با اضافه کردن این بخش به متغیر ordering_fields در فایل views.py  دسترسی پیدا میکنیم که میتوان فیلد های قابل مرتب سازی را در آن وارد کرد مانند تکه کد زیر

```python
ordering_fields = ['created', 'status']
```

دسترسی به این بخش از قسمت url ها بصورت پارمتر مانند آدرس زیر است

```
http://127.0.0.1:8000/Law/?ordering=crearted
```

