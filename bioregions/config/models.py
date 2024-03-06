from django.db import models


class NamedModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract=True

    def __str__(self):
        return self.name