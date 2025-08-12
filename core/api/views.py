from core import views
from core.models import Game, GameComment, ContactForm, Career, CareerForm, Founder, SocialMedia, SiteSettings
from core.api.serializers import (
    GameSerializer, GameRetrieveSerializer, GameCommentSerializer, ContactFormSerializer, CareerSerializer,
    CareerFormSerializer, FounderSerializer, SocialMediaSerializer, SiteSettingsSerializer
)
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameRetrieveAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameRetrieveSerializer

class GameCommentListAPIView(ListAPIView):
    queryset = GameComment.objects.all()
    serializer_class = GameCommentSerializer

class ContactFormCreateAPIView(CreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class CareerListAPIView(ListAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer