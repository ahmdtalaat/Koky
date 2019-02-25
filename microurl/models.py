from django.db import models


class MicroUrl(models.Model):
    longurl = models.URLField()
    shorturl = models.CharField(max_length=255, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.longurl
