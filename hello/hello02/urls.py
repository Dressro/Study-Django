from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello),
    path('var01',views.var01),
    path('var02',views.var02),
    path('for',views.forLoop),
]