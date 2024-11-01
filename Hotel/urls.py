# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.room_list, name='room_list'),
#     path('book/<int:room_id>/', views.book_room, name='book_room'),
# ]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   
]
