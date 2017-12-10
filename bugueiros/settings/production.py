from .base import  *


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd4hgjlihk1j4dc',
        'USER': 'owunjegqzpovqn',
        'PASSWORD': 'abc76cc97ab839fc5d999aecae0e840d4973f72eb24b82fefdcfa3314aae0d31',
        'HOST': 'ec2-54-235-213-202.compute-1.amazonaws.com',
        'PORT': '5432',
    }
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
}