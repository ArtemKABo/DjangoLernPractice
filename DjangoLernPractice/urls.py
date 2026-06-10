from django.urls import path 
from Tittles import views as tittle

urlpatterns = [
    path('', tittle.index)
]
