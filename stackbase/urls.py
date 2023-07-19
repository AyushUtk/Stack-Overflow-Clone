from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('',views.home, name="home"),

    #CRUD Functions
    path('questions/', views.QuestionListView.as_view(), name="question-lists"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name="question-detail"),
    path('questions/new/', views.QuestionCreateView.as_view(), name="question-create"),
    path('questions/<int:pk>/update/', views.QuestionUpdateView.as_view(), name="question-update"),
]