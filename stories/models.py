from django.db import models

# Create your models here.
class Story(models.Model):
    story_title = models.TextField(default="")
    story_content = models.TextField(default="")
    def __str__(self):
        return self.story_title+', '+self.story_content