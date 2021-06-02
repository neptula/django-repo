
from django.urls import path

from sec_app import views

urlpatterns=[
       path('help/',views.help,name='help'),
       path('home/',views.home,name='home'),
    path('form_/',views.form_,name='form'),
    path('contact/',views.contact,name='index'),
    path('user/',views.contactuser,name='index'),
]