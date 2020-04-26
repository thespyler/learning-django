from . import views
from django.urls import path
urlpatterns =[
	path('todo/', views.About_me)
]