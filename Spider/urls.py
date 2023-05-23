"""BS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Spider.views import GetConfig, GetAllTasks, GetSqlTasks, DelSqlTask, GetXssTasks, DelXssTask, TenDaysTasks, \
    TenDaysResNum, TenDaysTaskProcNum, TenDaySqlResGrade, TenDayXssResGrade, TaskHdr, SqlTasks, XssTasks,GetRes

urlpatterns = [
    path('GetConfig/', GetConfig, name='GetConfig'),
    path('GetAllTasks/', GetAllTasks, name='GetAllTask'),
    path('GetSqlTasks/', GetSqlTasks, name='GetSqlTask'),
    path('DelSqlTask/', DelSqlTask, name='DelSqlTask'),
    path('GetXssTasks/', GetXssTasks, name='GetXssTask'),
    path('DelXssTask/', DelXssTask, name='DelXssTask'),
    path('GetRes/', GetRes, name='GetRes'),

    path('TenDayTaskNum/', TenDaysTasks, name='TenDaysTasks'),
    path('TenDayResNum/', TenDaysResNum, name='TenDaysResNum'),
    path('TenDayTaskProcNum/', TenDaysTaskProcNum, name='TenDaysTaskProcNum'),
    path('TenDaySqlResGrade/', TenDaySqlResGrade, name='TenDaySqlResGrade'),
    path('TenDayXssResGrade/', TenDayXssResGrade, name='TenDayXssResGrade'),
    path('SqlTasks/', SqlTasks, name='SqlTasks'),
    path('XssTasks/', XssTasks, name='XssTasks'),
    path('TaskHdr/', TaskHdr, name='TaskHdr'),

]
