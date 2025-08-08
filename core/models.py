from django.db import models
from tinymce.models import HTMLField

class Game(models.Model):
    name = models.CharField(max_length=50)
    gametype = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    logo = models.ImageField(upload_to="gamepro_imgs/")
    image1 = models.ImageField(upload_to="gamepro_imgs/")
    image2 = models.ImageField(upload_to="gamepro_imgs/")
    about_title = models.CharField(max_length=200)
    about_content = models.TextField()
    app_address1 = models.URLField(max_length=200)
    app_address2 = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class GameComment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comment")
    username = models.CharField(max_length=30)
    comment = models.TextField()
    rait = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class ContactForm(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    mail = models.EmailField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.name

class Career(models.Model):
    image = models.ImageField(upload_to="gamepro_imgs/")
    title = models.CharField(max_length=50)
    content = models.TextField()
    about = HTMLField()

    def __str__(self):
        return self.title

class CareerForm(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    cv_url = models.URLField(max_length=256)
    linkedin_url = models.URLField(max_length=256)
    text = models.TextField()

    def __str__(self):
        return self.name

class Founder(models.Model):
    image = models.ImageField(upload_to="gamepro_imgs/")
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name