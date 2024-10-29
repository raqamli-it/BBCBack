from django.db import models


class Info(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='media/info/files/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'
