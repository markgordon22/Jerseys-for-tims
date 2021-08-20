from django.urls import path
from . import views
from contact import views as contact

urlpatterns = [
    path('', views.contact, name='contact'),
]