from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('rooms/<str:pk>/', views.rooms, name="rooms"), # Hakikisha jina la "rooms" linafanana na function mpya
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    
]