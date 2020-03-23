from django.urls import path

from systems import views

urlpatterns = [
    path('info/', views.listcustomers),
]
