from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.CourseViewSet.as_view(
        {'get': 'list'}
    )),
    path('viewset/student/', views.StudentListCreateAPIView.as_view(
    )),
    path('viewset/mentors/<int:pk>/', views.MentorRetrieveUpdateDestroyAPIView.as_view())
]