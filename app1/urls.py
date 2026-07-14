from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('IG/',views.ImageGallery,name='ImageGallery'),
    path('about/',views.about,name="aboutname"),
    path('condition/',views.student,name="studentname"),
    path('child/',views.templateInheritance,name="childname")
]