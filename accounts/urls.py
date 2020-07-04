from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

app_name = 'accounts'

urlpatterns = [
   #url(r'^login/$',views.LoginPageView,name='login'),
    url(r'^create/$',views.UserCreationView.as_view(),name='userCreationForm'),
    url(r'^login/$', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$',auth_view.LogoutView.as_view(),name='logout'),
    url(r'^profile/$',views.ProfileView.as_view(),name="profile"),
]
