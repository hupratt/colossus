import os, dotenv

from celery import Celery

# Load .env variables
if os.environ.get("DJANGO_DEVELOPMENT") == "true":
    dotenv.read_dotenv("/home/ubuntu/Dev/posthog/.env.development")
else:
    dotenv.read_dotenv("/home/ubuntu/Dev/posthog/.env")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "colossus.settings")

app = Celery("colossus")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
