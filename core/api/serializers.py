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

class CareerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerForm
        fields = "__all__"

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"