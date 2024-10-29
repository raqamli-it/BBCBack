from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/slider/image/', blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'
