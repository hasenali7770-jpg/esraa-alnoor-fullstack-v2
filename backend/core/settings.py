import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "change-me")
DEBUG = os.getenv("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
  "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions",
  "django.contrib.messages","django.contrib.staticfiles",
  "rest_framework","corsheaders","api",
]

MIDDLEWARE = [
  "corsheaders.middleware.CorsMiddleware",
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF="core.urls"

TEMPLATES=[{
  "BACKEND":"django.template.backends.django.DjangoTemplates",
  "DIRS":[],
  "APP_DIRS":True,
  "OPTIONS":{"context_processors":[
    "django.template.context_processors.debug",
    "django.template.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
  ]},
}]

WSGI_APPLICATION="core.wsgi.application"

DATABASES={"default": dj_database_url.config(default=os.getenv("DATABASE_URL"))}

AUTH_PASSWORD_VALIDATORS=[]
LANGUAGE_CODE="en-us"
TIME_ZONE="UTC"
USE_I18N=True
USE_TZ=True

STATIC_URL="static/"
STATIC_ROOT=os.path.join(BASE_DIR,"staticfiles")
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS=True

REST_FRAMEWORK={
  "DEFAULT_AUTHENTICATION_CLASSES":["api.auth.SupabaseJWTAuthentication"],
  "DEFAULT_PERMISSION_CLASSES":["rest_framework.permissions.AllowAny"],
}

SUPABASE_JWT_SECRET=os.getenv("SUPABASE_JWT_SECRET","")
ADMIN_EMAILS=[e.strip().lower() for e in os.getenv("ADMIN_EMAILS","").split(",") if e.strip()]
