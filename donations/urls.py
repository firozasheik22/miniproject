from django.urls import path
from . import views

urlpatterns=[
    path('receive',views.receive,name="receive"),
    path('donate',views.donate,name="donate")
]