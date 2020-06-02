import os
import string

from django.contrib.messages import constants as messages_constants

import dj_database_url
from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ==============================================================================
# CORE SETTINGS
# ==============================================================================


SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", False)


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "debug_toolbar",
    "crispy_forms",
    "colossus.apps.accounts",
    "colossus.apps.campaigns",
    "colossus.apps.core",
    "colossus.apps.templates",
    "colossus.apps.lists",
    "colossus.apps.notifications",
    "colossus.apps.subscribers",
]

SITE_ID = 1

ROOT_URLCONF = "colossus.urls"

WSGI_APPLICATION = "colossus.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "colossus",
        "USER": os.environ.get("dbuser"),
        "PASSWORD": os.environ.get("dbpassword"),
        "HOST": os.environ.get("hostip"),
        "PORT": os.environ.get("pnumber"),
    }
}

INTERNAL_IPS = ["127.0.0.1", "localhost"]


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "colossus.apps.accounts.middleware.UserTimezoneMiddleware",
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "colossus/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "colossus.apps.notifications.context_processors.notifications",
            ],
        },
    },
]

# ==============================================================================
# INTERNATIONALIZATION AND LOCALIZATION SETTINGS
# ==============================================================================

LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", "en-us")

TIME_ZONE = os.environ.get("TIME_ZONE", "Europe/Luxembourg")

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ("en-us", "English"),
    ("pt-br", "Portuguese"),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, "colossus/locale"),)


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "colossus/static"),
]


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media/public")

PRIVATE_MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media/private")


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_SUBJECT_PREFIX = "[Colossus] "

SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "root@localhost")

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "webmaster@localhost")

EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost")

EMAIL_PORT = os.environ.get("EMAIL_PORT", 587)

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "root")

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LOGIN_REDIRECT_URL = "campaigns:campaigns"


# ==============================================================================
# DJANGO CONTRIB APPS SETTINGS
# ==============================================================================

MESSAGE_TAGS = {
    messages_constants.DEBUG: "alert-dark",
    messages_constants.INFO: "alert-primary",
    messages_constants.SUCCESS: "alert-success",
    messages_constants.WARNING: "alert-warning",
    messages_constants.ERROR: "alert-danger",
}

if DEBUG:
    MESSAGE_LEVEL = messages_constants.DEBUG
else:
    MESSAGE_LEVEL = messages_constants.INFO

GEOIP_PATH = os.path.join(BASE_DIR, "bin/GeoLite2")


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

CRISPY_TEMPLATE_PACK = "bootstrap4"

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")

CELERY_BEAT_SCHEDULE = {
    "send-scheduled-campaigns": {
        "task": "colossus.apps.campaigns.tasks.send_scheduled_campaigns_task",
        "schedule": 60.0,
    },
    "clean-lists-hard-bounces": {
        "task": "colossus.apps.lists.tasks.clean_lists_hard_bounces_task",
        "schedule": crontab(hour=12, minute=0),
    },
}

CELERY_TASK_ALWAYS_EAGER = os.environ.get("CELERY_TASK_ALWAYS_EAGER", True)


# ==============================================================================
# FIRST-PARTY APPS SETTINGS
# ==============================================================================

COLOSSUS_HTTPS_ONLY = os.environ.get("COLOSSUS_HTTPS_ONLY", False)

MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY", "")

MAILGUN_API_BASE_URL = os.environ.get("MAILGUN_API_BASE_URL", "")

MAILJET_API_KEY = os.environ.get("MAILJET_API_KEY", "")
MAILJET_API_SECRET = os.environ.get("MAILJET_API_SECRET", "")
