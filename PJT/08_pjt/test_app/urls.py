from django.urls import path
from . import views

urlpatterns = [
    path('test_a/', views.test_a),
    path('test_b/', views.test_b),
    path('test_c/', views.test_c),
]

