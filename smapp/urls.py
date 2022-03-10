from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('search/',views.lot_details,name='lot_details'),
]

#Configure Admin title
admin.site.site_header="Smeat Administration"