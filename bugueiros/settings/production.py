from .base import  *


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd9jm4p9joa4irh',
        'USER': 'twxbuigxkboycu',
        'PASSWORD': '6de14b30bc4efb4c177c4cbeca256be6329ad1d7e52d1e066c55f5d531fad925',
        'HOST': 'ec2-54-163-230-219.compute-1.amazonaws.com',
        'PORT': '5432',
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
}