from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('scrape', views.scrape_handler, name='scrape'),
]
