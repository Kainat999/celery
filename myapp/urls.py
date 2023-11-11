from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.about, name='about'),
    path('', views.contact, name='contact'),
]
