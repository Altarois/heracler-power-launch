
from django.urls import path
from . import views

urlpatterns = [
    #path('client', views.clients , name='client'),
    path('', views.home , name='homeClient'),
    path('session/<str:session_id>', views.clients_session, name='Csession')
]
