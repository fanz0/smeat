from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('search/',views.lot_details,name='lot_details')
]