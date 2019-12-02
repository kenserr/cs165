"""cs165 URL Configuration

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
from pages.views import home_view, read_view
from passport_stat.views import passport_stat_create_view, passport_stat_list_view
from emergency_contact.views import emergency_contact_update_view, emergency_contact_create_view, emergency_contact_list_view, emergency_contact_detail_view
from passport_holder.views import passport_holder_delete_view, passport_holder_detail_view, passport_holder_create_view, passport_holder_list_view, passport_holder_update_view


urlpatterns = [
	path('', home_view, name='home'),
	path('ph/new/', passport_holder_create_view),
    path('ph/all/', passport_holder_list_view),
    path('ph/<int:id>/', passport_holder_detail_view, name='phview'),
    path('ph/<int:id>/update/', passport_holder_update_view),
    path('ph/<int:id>/delete', passport_holder_delete_view),
    path('admin/', admin.site.urls),
    path('read/', read_view, name='read'),
    path('ps/new/', passport_stat_create_view),
    path('ps/all/', passport_stat_list_view),
    path('ec/new/', emergency_contact_create_view),
    path('ec/all/', emergency_contact_list_view),
    path('ec/<str:name>/', emergency_contact_detail_view),
    path('ec/<str:name>/update/', emergency_contact_update_view),
]
