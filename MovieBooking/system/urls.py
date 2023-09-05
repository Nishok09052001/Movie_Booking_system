from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('movies/<int:id>',views.movies,name='movies'),
    path('logout',views.logout,name='logout'),
    
    path('register',views.register,name='register')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)