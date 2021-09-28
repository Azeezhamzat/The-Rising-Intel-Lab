# replace 'your.domain' with your desired domain
BASE_URL = 'https://therisingintellab.online'
ALLOWED_HOSTS = [u'therisingintellab.online', u'localhost']

# database config - we recommend postgresql for production purposes
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'aplus-test-database',
  }
}

# forward outgoing emails to a local email proxy
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='127.0.0.1'

# folder for user-uploads, directly served from the webserver (see nginx example below). Must be created manually.
MEDIA_ROOT='/home/aplus/aplus-media'

# replace the value below with some random value
SECRET_KEY = u'print('AAAAB3NzaC1yc2EAAAABJQAAAQEAjlsiQ8jcEyIgAh2FeasSq4qzMxnpQEGDMoxC')

# some basic security settings for serving the website over https - see django docu
CSRF_COOKIE_SECURE=True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_HTTPONLY = True

FILE_UPLOAD_PERMISSIONS = 0o644