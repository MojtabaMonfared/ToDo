from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=200, blank=True, null=False)
    description = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    status = models.BooleanField(name="Done?", default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "tasks"
        ordering = ["-priority"]