"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from company.views import data_page, data_things, data_exclusive, data_GetUpdate, data_MainBanner, data_VacationPlan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', data_page, name='home'),
    path('thing', data_things, name='things'),
    path('exclusive', data_exclusive),
    path('getUpdate', data_GetUpdate),
    path('mainBanner', data_MainBanner),
    path('vacationPlan', data_VacationPlan)
]
