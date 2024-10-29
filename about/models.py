from django.db import models


class Top(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/about/image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Top'
        verbose_name_plural = 'Top'


class Workers(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/about/image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'


class Social(models.Model):
    worker = models.ForeignKey(Workers, related_name='socials', on_delete=models.CASCADE)
    social_name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.social_name} - {self.worker.name}"

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'


class Services(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    svg_icon = models.FileField(upload_to='media/about/image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

