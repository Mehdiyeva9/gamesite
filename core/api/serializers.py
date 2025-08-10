from rest_framework import serializers
from core.models import Game, GameComment, ContactForm, Career, CareerForm, Founder, SocialMedia, SiteSettings

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("name", "gametype", "content", "logo")

class GameRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class GameCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameComment
        fields = "__all__"

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"