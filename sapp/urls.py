from django.urls import path
from . import  views
app_name='sapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
     path('reg/',views.reg,name='reg'),
    path('welcome/',views.newpage,name='newpage'),
    path('setupprofile/',views.profile,name='profile'),
    path('tnx/',views.tnx,name='tnx')
]
