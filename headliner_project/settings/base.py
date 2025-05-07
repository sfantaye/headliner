# headliner_project/settings/base.py
import os
import environ # Add this import

# ... (other imports)

# Initialize django-environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Assuming .env file is in the project root (headliner/)
environ.Env.read_env(os.path.join(BASE_DIR, '..', '.env')) # Go one level up for .env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='your-development-secret-key') # Use environ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True) # Use environ

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1']) # Use environ

# Application definition
INSTALLED_APPS = [
    # Custom apps first
    'news',
    'site_settings', # We'll create this for site-wide settings
    'core', # For general utilities, custom user if needed

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.contrib.modeladmin', # Useful for managing non-Page models
    'wagtail.contrib.routable_page', # For custom routing
    'wagtail.contrib.sitemaps', # For sitemap.xml
    'wagtail.api.v2', # If you plan to use Wagtail API
    'wagtail_headless_preview', # If considering headless preview
    'wagtail.contrib.settings', # For site settings
    'wagtailmenus', # For navigation menus
    'taggit', # For tagging
    'modelcluster', # For ParentalKey, etc.

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps', # Django sitemaps, Wagtail has its own

    # Tailwind (if using wagtail-tailwind)
    'tailwind',
    'theme', # Our Tailwind theme app
    'compressor', # For django-compressor
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Whitenoise
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'headliner_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings', # Wagtail settings
                'wagtailmenus.context_processors.wagtailmenus', # For wagtailmenus
            ],
        },
    },
]

WSGI_APPLICATION = 'headliner_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3') # Use environ
}
# Example .env for PostgreSQL:
# DATABASE_URL=postgres://user:password@host:port/dbname

# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    # ... (default validators)
]

# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder', # For django-compressor
]
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_collected') # For collectstatic
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Wagtail settings
WAGTAIL_SITE_NAME = 'Headliner News'
WAGTAIL_ENABLE_UPDATE_CHECK = False # Optional: disable update check messages
WAGTAILADMIN_BASE_URL = 'http://localhost:8000' # Or your domain

# Search backend (default is database, good for starting)
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Tailwind settings (if using wagtail-tailwind)
TAILWIND_APP_NAME = 'theme'
NPM_BIN_PATH = '/usr/local/bin/npm' # Adjust if your npm is elsewhere, or use ` shutil.which('npm') `
# For Windows, it might be:
# NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# django-compressor settings (if using tailwind)
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False # Set to True for production builds
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/tailwindcss', 'django_tailwind_cli.filters.TailwindCliFilter'),
)

# Wagtail settings for custom image model (optional, but good practice for future extension)
# WAGTAILIMAGES_IMAGE_MODEL = 'core.CustomImage'
# WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False # If not using it

# For robots.txt (can be a static file or handled by a view/Wagtail setting)
# We'll use wagtail.contrib.settings later.