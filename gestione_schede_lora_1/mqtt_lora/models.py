from django.db import models

# Create your models here.
class Scheda(models.Model):
    add_h = models.IntegerField()
    add_l = models.IntegerField()
    chan = models.IntegerField()

    def __str__(self) -> str:
        return f"add_h: {self.add_h}, add_l: {self.add_l}, chan: {self.chan}"

class Topic(models.Model):
    nome = models.TextField(max_length=32, unique=True)
    schede = models.ManyToManyField(Scheda, blank=True, related_name="topics")

    def __str__(self) -> str:
        return self.nome
    
class DataBaseMessage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    message_content = models.TextField(max_length=100)
    retain = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now_add=True)
