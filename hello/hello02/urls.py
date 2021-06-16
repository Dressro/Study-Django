from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello,name='index'),
    path('var01',views.var01),
    path('var02',views.var02),
    path('for',views.forLoop),
    path('if01',views.if01),
    path('if02',views.if02),
    path('href',views.href)
]