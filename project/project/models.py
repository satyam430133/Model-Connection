from django.db import models

class ModelA(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ModelB(models.Model):
    model_a = models.ForeignKey(ModelA, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description