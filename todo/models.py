from django.db import models


# This table consists of 2 columns: task, and creation date
class Todo(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.task
