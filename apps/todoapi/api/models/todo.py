from django.db import models


class Todo(models.Model):
    TRIM_TITLE_LEN = 50
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    url = models.URLField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.__class__.__name__}(title={self.title[:self.TRIM_TITLE_LEN]}, is_completed={self.is_completed})"

