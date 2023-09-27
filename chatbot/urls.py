from django.urls import path
from chatbot import views

app_name = 'chatbot'

urlpatterns = [
    path('chat/', views.chat_message, name='chat'),
    path('chat/history/', views.chat_history, name='chat_history'),
]
