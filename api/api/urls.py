"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # add this
from rest_framework import routers  # add this
from articles import urls  # add this
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include



#router = routers.DefaultRouter()  # add this
#router.register(r'articles', views.ArticleListView, 'articles')  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include("articles.urls")),  # add this
    path('token-auth/', obtain_jwt_token),  # add this
    path('core/', include('core.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
