from django.contrib import admin
from django.urls import path, include

urlpatterns = [

path('admin/', admin.site.urls),

#connect path to cookBook_app urls
path('', include('nba_forum.urls')),

]
