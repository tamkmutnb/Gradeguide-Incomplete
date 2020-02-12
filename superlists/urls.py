from django.conf.urls import url
from lists import views

from django.urls import path, include
from django.contrib import admin

#from superlists

urlpatterns = [
    path('', views.register, name='register'),
    path('calGrade',views.calGrade,name='calGrade'),
    path('termselect',views.termselect,name='termselect'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'home', views.home_page, name='home'),
    #admin page
    #path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    #register path
    #path("register/", v.register, name="register"),


]
