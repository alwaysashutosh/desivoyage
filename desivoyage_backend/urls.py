"""
URL configuration for desivoyage_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from desivoyage import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('redirect/', views.redirect_view, name='redirect'),
    path('logout/', views.logout_view, name='logout'),
    path('book/', views.book_view, name='book'),
    path('/login/register/', views.register_view, name='register'),
    path('/login/redirect/', views.redirect_view, name='redirect'),
    path('/login/logout/', views.logout_view, name='logout'),
    path('/login/book/', views.book_view, name='book'),
    path('/login/register/login.html', views.login_view, name='login'),
    path('/login/register/register.html', views.register_view, name='register'),
    path('/login/register/index.html', views.home, name='home'),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
