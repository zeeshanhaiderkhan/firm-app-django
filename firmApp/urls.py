from django.contrib import admin
from django.urls import path,include
from accounts import urls
from django.contrib.auth.views import LoginView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
]
