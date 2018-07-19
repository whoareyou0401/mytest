from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^first$", first_celery),
    url(r"^poetry$", create_poetry_czn)
]