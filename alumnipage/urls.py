from django.urls import path, include
from alumnipage import views

urlpatterns = [
    path('alumni_data/', views.StandardAPIView.as_view()),
    path('get_alumnidata/<int:pk>/', views.StandardAPIView.as_view()),
]
