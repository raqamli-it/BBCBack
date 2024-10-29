from django.db import models


class Logo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='media/logo/image/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logos'


class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    km = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    image = models.FileField(upload_to='media/car/image/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE, blank=True, null=True)
    automatic = models.BooleanField(default=False, blank=True, null=True)
    mechanic = models.BooleanField(default=False,blank=True, null=True)
    discount = models.BooleanField(default=False,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Image(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/car/image/')

    def __str__(self):
        return self.image.url


class InstallmentPlan(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='installment_plans', blank=True, null=True)

    def __str__(self):
        return self.car.title if self.car else "No Car"


class Sub(models.Model):
    duration = models.PositiveIntegerField(blank=True, null=True)  # months
    prepayment_percentage = models.PositiveIntegerField(blank=True, null=True)  # percentage
    annual_interest_rate = models.FloatField(blank=True, null=True)  # annual interest rate
    installmentplan = models.ForeignKey(InstallmentPlan, on_delete=models.CASCADE, related_name='subs')

    def __str__(self):
        return f"{self.duration} months - {self.prepayment_percentage}% prepayment - {self.annual_interest_rate}% annual interest"

    class Meta:
        unique_together = ('installmentplan', 'duration')
        ordering = ('duration',)
        verbose_name = 'sub'
        verbose_name_plural = 'subs'
