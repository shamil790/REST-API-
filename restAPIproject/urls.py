"""restAPIproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from restapp import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/',views.helloworldView.as_view()),
    path('name/',views.name.as_view()),
    path('operations/add', views.AddNumbersView.as_view()),
    path('CubeView/',views.CubeView.as_view()),
    path('Fcatorialclass/', views.Fcatorialclass.as_view()),
    path('primeView/', views.primeView.as_view()),
    path('register/', views.register.as_view(),name="register"),
    path('login/',obtain_auth_token,name="login")


]