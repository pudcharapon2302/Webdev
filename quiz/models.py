from django.db import models

class question(models.Model):
    text = models.CharField(max_length=100)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.text
    
class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    correct = models.BooleanField()

    def __str__(self):
        return self.text
