from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    url = models.URLField()
    order = models.IntegerField()

    def __repr__(self):
        return f"{self.title} - {self.is_completed}"

