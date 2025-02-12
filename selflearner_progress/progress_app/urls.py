from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add_course/', views.add_course, name='add_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/add_topic/', views.add_topic, name='add_topic'),
    path('topic/<int:topic_id>/toggle/', views.toggle_completion, name='toggle_completion'),
    path('progress/', views.progress_view, name='progress'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('topic/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
]
