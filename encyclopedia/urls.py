from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.singleEntry,name='singleEntry'),
    path('wiki/create/Encyc', views.creatEntry, name='createEntry'),
    path('wiki/random/Encyc',views.randomPage,name='randomPage'),
    path('wiki/<str:title>/edit/',views.editEntry,name='editEntry')
]
