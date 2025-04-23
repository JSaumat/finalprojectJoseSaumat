"""
URL configuration for finalprojectJoseSaumat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
from django.contrib import admin

from django.urls import include, path

# Main URL patterns Django uses to route requests made
urlpatterns = [

    # The admin interface which is accessible at /admin/
    path("admin/", admin.site.urls),

    # App level URLs from the movies/urls.py file.
    path('', include('movies.urls')),

    #App level URLSs from the forum/urls.py file.
    path("forum/", include("forum.urls", namespace="forum")),

]
