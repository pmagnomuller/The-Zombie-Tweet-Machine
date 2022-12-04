from django.db import models
from .utils import create_tweet

# Create your models here.

class TextBlock(models.Model):
    text = models.TextField(blank=True)
    tweet = models.TextField(blank=True)

    def save(self) -> None:
        prompt = {}
        prompt["hashtag"] = "#thethoughtmachine" 
        prompt["text"] = "Write an engaging, controversial tweet that has a high probability of getting viral or trending using these words:" + self.text
        thething = create_tweet(prompt)
        self.tweet = thething
        print(thething)
        return super().save()



    def __str__(self):
        return f"{self.text} {self.tweet}"