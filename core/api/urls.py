from django.conf import urls
from django.urls import path
from core.api import views

urlpatterns = [
    path('game-list/', views.GameListAPIView.as_view()),
    path('game-retrieve/<id>/', views.GameRetrieveAPIView.as_view()),
    path('game-comment-list/', views.GameCommentListAPIView.as_view()),
    path('contactform-create/', views.ContactFormCreateAPIView.as_view()),
]