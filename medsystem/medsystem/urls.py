"""medsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from meds.views import RegisterFormView, LoginFormView, LogoutView, IndexView, AdviceCreateView, ProfileCreateView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^category/(?P<pk>[0-9a-f\-]+)/$', IndexView.as_view()),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^advice/$', AdviceCreateView.as_view(), name='advice'),
    url(r'^add_profile/$', ProfileCreateView.as_view()),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),


] + static(settings.STATIC_URL, document_root='meds/static/')
