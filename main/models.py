from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Текст варианта ответа', max_length=100)
    is_correct = models.BooleanField('Правильный ответ', default=False)

class Test(models.Model):
    title = models.CharField('Вопрос', max_length=100)
    questions = models.ManyToManyField(Question)

class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.FloatField('Результат теста')

    class Meta:
        unique_together = ('test', 'user')
