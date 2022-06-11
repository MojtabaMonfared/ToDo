from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    # status = models.BooleanField(name="Done?", default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "tasks"
        ordering = ["-priority"]