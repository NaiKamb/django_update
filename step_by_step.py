# nailya@nailya-Aspire-E5-575G:~$ cd Desktop/
# nailya@nailya-Aspire-E5-575G:~/Desktop$ cd py30/
# nailya@nailya-Aspire-E5-575G:~/Desktop/py30$ cd django/
# nailya@nailya-Aspire-E5-575G:~/Desktop/py30/django$ ls
# admini  images  intro.py  manage.py  requirements.txt  terminal.py  test1  venv
# nailya@nailya-Aspire-E5-575G:~/Desktop/py30/django$ cd ..
# nailya@nailya-Aspire-E5-575G:~/Desktop/py30$ mkdir new_django_project
# nailya@nailya-Aspire-E5-575G:~/Desktop/py30$ cd new_django_project/
# nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ python3 -m venv venv
# nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ . venv/bin/activate
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ nano requirements.txt
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ pip3 install -r requirements.txt 
                                    # Collecting django
                                    #   Using cached Django-4.2.4-py3-none-any.whl (8.0 MB)
                                    # Collecting djangorestframework
                                    #   Using cached djangorestframework-3.14.0-py3-none-any.whl (1.1 MB)
                                    # Collecting psycopg2-binary
                                    #   Using cached psycopg2_binary-2.9.7-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
                                    # Collecting python-decouple
                                    #   Downloading python_decouple-3.8-py3-none-any.whl (9.9 kB)
                                    # Collecting drf-yasg
                                    #   Downloading drf_yasg-1.21.7-py3-none-any.whl (4.3 MB)
                                    #      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 496.2 kB/s eta 0:00:00
                                    # Collecting sqlparse>=0.3.1
                                    #   Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
                                    # Collecting asgiref<4,>=3.6.0
                                    #   Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
                                    # Collecting pytz
                                    #   Using cached pytz-2023.3-py2.py3-none-any.whl (502 kB)
                                    # Collecting inflection>=0.3.1
                                    #   Downloading inflection-0.5.1-py2.py3-none-any.whl (9.5 kB)
                                    # Collecting pyyaml>=5.1
                                    #   Downloading PyYAML-6.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (705 kB)
                                    #      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 705.5/705.5 KB 628.3 kB/s eta 0:00:00
                                    # Collecting packaging>=21.0
                                    #   Downloading packaging-23.1-py3-none-any.whl (48 kB)
                                    #      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.9/48.9 KB 378.9 kB/s eta 0:00:00
                                    # Collecting uritemplate>=3.0.0
                                    #   Downloading uritemplate-4.1.1-py2.py3-none-any.whl (10 kB)
                                    # Collecting typing-extensions>=4
                                    #   Using cached typing_extensions-4.7.1-py3-none-any.whl (33 kB)
                                    # Installing collected packages: pytz, python-decouple, uritemplate, typing-extensions, sqlparse, pyyaml, psycopg2-binary, packaging, inflection, asgiref, django, djangorestframework, drf-yasg
                                    # Successfully installed asgiref-3.7.2 django-4.2.4 djangorestframework-3.14.0 drf-yasg-1.21.7 inflection-0.5.1 packaging-23.1 psycopg2-binary-2.9.7 python-decouple-3.8 pytz-2023.3 pyyaml-6.0.1 sqlparse-0.4.4 typing-extensions-4.7.1 uritemplate-4.1.1
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ django-admin startproject config .
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ ls
# config  manage.py  requirements.txt  venv
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ code .
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ mkdir apps
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ cd apps
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project/apps$ ../manage.py startapp main
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project/apps$ ls
# main
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project/apps$ cd ..
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ ls
# apps  config  manage.py  requirements.txt  venv
# (venv) nailya@nailya-Aspire-E5-575G:~/Desktop/py30/new_django_project$ psql
# psql (14.8 (Ubuntu 14.8-0ubuntu0.22.04.1))
# Type "help" for help.

# nailya=# CREATE DATABASE new_django_db;
# CREATE DATABASE
# nailya=# 
'''------------------------------------------------------'''
# in settings.py:

# from decouple import config - для сокрытия личных данных(пароль и тд)

# SECRET_KEY = config('SECRET_KEY')  тут можно сгенерировать ключ https://djecrety.ir/

# далее добавить: 
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
    
#     #libs
#     'rest_framework',
    
#     #apps
#     'apps.main',
# ]

# изменить базу данных:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASS'),
#         'HOST': 'localhost',
#         'PORT': 5432
#     }
# }
'''======================================'''
# создать в config файл .env:
    
# SECRET_KEY=2^&y28^=ws1f5rcy8bm*gw&ap71rl**fznxiwr93szf5uf&c@8
# тут можно сгенерировать ключ https://djecrety.ir/

# #database
# DB_NAME=new_django_db
# DB_USER=nailya
# DB_PASS=1
'''======================================'''
# изменить в urls.py /config
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('posts/', include('apps.main.urls'))
# ]
'''============================'''
# создать urls.py в apps/main

# from django.urls import path
# from .views import post_list, create_post

# urlpatterns = [
#     # path('posts/', post_list),
#     path('', post_list),
#     path('create/', create_post),
#     path('delete/<int:post_id>/',delete_post)
# ]
'''============================'''
# добавить в models.py /apps/main

# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model() #достает юзера из под капота django

# # для создания таблиц в постгрес, модели=таблицы
# class Post(models.Model):
#     author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f'{self.author.username} -> {self.body}'
'''============================'''
# создать в apps/main serializers.py

# from rest_framework import serializers
# from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
'''============================='''
# в apps.py/main добавить:
# from django.apps import AppConfig


# class MainConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'apps.main'

'''============================='''
# добавитьт в admin.py/main:
    
# from django.contrib import admin

# # Register your models here.

# from .models import Post

# admin.site.register(Post)
'''============================'''
# в views.py/apps/main добавить:
    
# from django.contrib.auth import get_user_model
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from .models import Post
# from .serializers import PostSerializer

# User = get_user_model()

# @api_view(['GET'])
# def post_list(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data, status=200)

# @api_view(['POST']) 
# def create_post(request):
#     serializer = PostSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response('Пост успешно создан', status=201)

# @api_view(['DELETE'])
# def delete_post(request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         post.delete()
#         return Response('Пост успешно удален', status=204)

