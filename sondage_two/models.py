from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.crypto import get_random_string

class SondageTwo(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255, default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = f"{base_slug}-{get_random_string(length=5)}"
        super().save(*args, **kwargs)

    def get_survey_url(self):
        return reverse('sondage-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title
    
class QuestionTwo(models.Model):
    sondage = models.ForeignKey(SondageTwo, on_delete=models.CASCADE, related_name='questions', default="1")
    question = models.TextField()


class ReponseTwo(models.Model):
    question = models.ForeignKey(QuestionTwo, on_delete=models.CASCADE, related_name='responses')
    reponse = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)


