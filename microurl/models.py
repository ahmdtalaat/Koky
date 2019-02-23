from django.db import models


class MicroUrl(models.Model):
    shorturl = models.CharField(max_length=100, unique=True)
    longurl = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.longurl
