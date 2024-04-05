from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.crypto import get_random_string


class Sondage(models.Model):
    question = models.TextField()
    options = models.JSONField(default=list)
    slug = models.SlugField(unique=True, max_length=255, default="")

    def add_option(self, option_text):
        self.options.append(option_text)
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.question)
            self.slug = f"{base_slug}-{get_random_string(length=5)}"
        super().save(*args, **kwargs)

    def get_survey_url(self):
        return reverse('sondage-detail', args=[str(self.pk)])

    def __str__(self):
        return f"Sondage: {self.question}"


class Answer(models.Model):
    sondage = models.ForeignKey(Sondage, on_delete=models.CASCADE, related_name='answers')
    choix = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer for Sondage: {self.sondage.id}"
