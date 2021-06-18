from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, null=True)
    is_completed = models.BooleanField(default=False, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
