"""hellobello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from restaurants.views import home,information,about,AboutView,AboutTemplateView
#from restaurants.views import HomeView,InformationView,AboutTemplateView,AboutView
from restaurants.views import HomeView,AboutView
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', home),
    #url(r'^information/$', information),
    #url(r'^about/$', about),
    #------------------------------------
    url(r'^$', HomeView.as_view()),                             #TemplateView
    #url(r'^information/$', InformationView.as_view()),          #TemplateView
    #url(r'^about/$', AboutTemplateView.as_view()),             #TemplateView
    url(r'^information/$', TemplateView.as_view(template_name='information.html')),          #TemplateView
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^about/(?P<id>\d+)/$', AboutView.as_view()),          #Class-based-View


]
