from django.urls import path
from . import views

urlpatterns = [
    path('color', views.color, name='color'),
    path('gradient', views.gradient, name='gradient'),
    path('pattern', views.pattern, name='pattern'),
    path("submit-pattern/", views.submit_pattern, name="submit-pattern"),
    path("submit-gradient/", views.submit_gradient, name="submit-gradient"),
    path("submit-color/", views.submit_color, name="submit-color"),
    path('', views.mainapp, name='home')
]
