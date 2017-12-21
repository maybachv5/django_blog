"""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# 替换数据库连接库
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2020wu)kcm-0(_7z^+!e$i8!d^qo&@^u72ht#m+%p_v#5g^)5a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.stopfollow.com']

# Application definition

INSTALLED_APPS = [

    'bootstrap_admin',  # 注册bootstrap后台管理界面,这个必须放在最前面

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # 添加人性化过滤器
    'django.contrib.sitemaps',  # 网站地图

    'oauth',  # 自定义用户应用
    # allauth需要注册的应用
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.github',

    'crispy_forms',  # bootstrap表单样式
    'imagekit',  # 上传图片的应用

    'haystack',  # 全用搜索应用 这个要放在其他应用之前
    'blog',  # 博客应用
    'comment',  # 评论应用

    'tools', # 工具应用

]

# allauth配置
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 自定义用户model
AUTH_USER_MODEL = 'oauth.Ouser'

# allauth需要的配置
# 当出现"SocialApp matching query does not exist"这种报错的时候就需要更换这个ID
SITE_ID = 10

# 设置登录和注册成功后重定向的页面，默认是/accounts/profile/
LOGIN_REDIRECT_URL = "/"

# Email setting
# 邮箱配置
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'stopfollow@163.com'
EMAIL_HOST_PASSWORD = 'django666'  # 这个不是邮箱密码，而是授权码
EMAIL_PORT = 465  # 由于阿里云的25端口打不开，所以必须使用SSL然后改用465端口
# 是否使用了SSL 或者TLS，为了用465端口，要使用这个
EMAIL_USE_SSL = True
# 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可用的邮箱
DEFAULT_FROM_EMAIL = 'Stopfollow <stopfollow@163.com>'
# 禁用注册邮箱验证
ACCOUNT_EMAIL_VERIFICATION = 'none'
# 登录方式，选择用户名或者邮箱都能登录
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# 设置用户注册的时候必须填写邮箱地址
ACCOUNT_EMAIL_REQUIRED = True
# 登出直接退出，不用确认
ACCOUNT_LOGOUT_ON_GET = True

# 表单插件的配置
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 设置视图
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'blog.context_processors.settings_info',  # 自定义上下文管理器
            ],
        },
    },
]

WSGI_APPLICATION = 'django_blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 修改数据库为MySQL，并进行配置
        'NAME': 'django_blog',
        'USER': 'root',
        'PASSWORD': 'python',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4', }
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 关闭国际时间，不然数据库报错

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# 静态文件收集
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 媒体文件收集
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 网站上下文信息
DEFAULT_IMG_LINL = 'http://cdn.stopfollow.com/summary_default.png'
SITE_DESCRIPTION = 'Django博客，一个后端使用Django框架，前端使用Bootstrap3搭建的个人博客网站，用于Python的学习和交流。'
SITE_KEYWORDS = 'Python Web开发,Python爬虫实例,Django博客教程,个人博客搭建'

# messages 标签设置，设置成bootstrap3样式
from django.contrib.messages import constants as message_constants

MESSAGE_TAGS = {
    message_constants.DEBUG: 'alert alert-primary alert-dismissible',
    message_constants.INFO: 'alert alert-info alert-dismissible',
    message_constants.SUCCESS: 'alert alert-success alert-dismissible',
    message_constants.WARNING: 'alert alert-warning alert-dismissible',
    message_constants.ERROR: 'alert alert-danger alert-dismissible'
}

# 全文搜索应用配置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',  # 选择语言解析器为自己更换的结巴分词
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),  # 保存索引文件的地址，选择主目录下，这个会自动生成
    }
}

# HAYSTACK_SIGNAL_PROCESSOR  =  'haystack.signals.BaseSignalProcessor'
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
