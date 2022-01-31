from atexit import register
from django.conf.urls import url
from django.urls import path, include
from DoctorApp import views

from django.conf.urls.static import static
from django.conf import settings

#Auth

from .views import LoginView, LogoutView, RegisterView, UserView

urlpatterns=[
    
    path('addpost',views.addpost),

    path('showpost',views.showpost),

    path('signin',views.signin),

    path('home',views.homepage),

    #path('signup',views.signup),

    path('register', RegisterView.as_view()),

    path('login', LoginView.as_view()),

    path('user', UserView.as_view()),

    path('logout', LogoutView.as_view()),
    

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)