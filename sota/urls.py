# -*- coding: UTF-8 -*-
# File Name：utils
# Author : Chen Quan
# Date：2019/5/7
# Description :
__author__ = 'Chen Quan'

from django.urls import path

from . import views

urlpatterns = [
    # path("/api?keyword=<str:keyword>&num_results=<int:num_results>", views.index, name='index'),
    # path("/api(?P<keyword>\d+)/(?P<num_results>\d+)$", views.index, name='index'),
    path("api", views.index, name='index'),
]
