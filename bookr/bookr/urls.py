
from django.contrib import admin
# from reviews.admin import admin_site
from django.urls import path, include
import reviews.views


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('reviews.urls')), 
]
