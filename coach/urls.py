
from django.urls import path
from . import views
from .views import  exo, sessionComplete, delete, add_exo, affiliate, show_session, attribute_session

#from users import user_views

urlpatterns = [
    path('', views.index),
    #path('list', views.listing),
    #path('list/<album_id>/', views.detail),
    path('search/', views.search),
    path('exo/', exo.as_view(), name='exo'),
    path('affiliate/', affiliate.as_view(), name='afi'),
    path('add_exo/', add_exo.as_view(), name='add_exo'),
    path('clients/<coach_id>', views.view_client),
    path('login', views.login),
    path('session',views.coach_session, name='session'),
    path('addsession/<str:session_id>',views.addsession, name='addsession'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('addclient',views.addclient, name='addclient'),
    path('pt_profile',views.pt_profile, name='pt_profile'),
    path('addsession/<str:id>/completed',sessionComplete.as_view(), name="complete"),
    path('addsession/<str:id>/deleted',delete.as_view(), name="delete"),
    path('addclient/<str:id>/added',show_session.as_view(), name="addC"),
    path('manage/<str:name>', views.attribute_session , name="manage")
]
