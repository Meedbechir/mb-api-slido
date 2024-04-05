from django.db import models

class QuestionThree(models.Model):
    question = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200, default="A")
    
    def __str__(self):
        return self.question

class ChoixThree(models.Model):
    question = models.ForeignKey(QuestionThree, on_delete=models.CASCADE)
    choix = models.JSONField()

    def __str__(self):
        return str(self.choix)

class ReponseThree(models.Model):
    question = models.OneToOneField(QuestionThree, on_delete=models.CASCADE)
    reponse = models.CharField(max_length=200)

    def __str__(self):
        return self.reponse
