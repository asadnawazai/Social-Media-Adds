from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.predict_view, name='predict_view'),
]