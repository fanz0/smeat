from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('search/',views.lot_details,name='lot_details'),
    path('lots_list/',views.lots_list,name='lots_list'),
    path('lot/<int:pk>/', views.single_lot, name='single_lot'),
    path('new_lot/', views.new_lot, name='new_lot'),
    path('lot/<int:pk>/edit/', views.lot_edit, name='lot_edit'),
]

#Configure Admin title
admin.site.site_header="Smeat Administration"