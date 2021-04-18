from django.urls import path     
from . import views
urlpatterns = [
    path('first_app/', views.index),
    path('first_app/new',views.new),
    path('first_app/create',views.create),
    path('first_app/<int:number>',views.show),
    path('first_app/<int:number>/edit',views.edit),
    path('first_app/<int:number>/delete',views.destroy),
]