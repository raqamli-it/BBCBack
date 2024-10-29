from django.contrib import admin

from catalog.models import Logo, Car, InstallmentPlan, Sub, Image


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'link', 'order',)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'automatic', 'mechanic', 'discount', 'created_at', 'updated_at', 'order',)
    search_fields = ('title',)
    inlines = [ImageInline]
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'price', 'year', 'km', 'color_uz', 'color_ru',
              'image', 'automatic', 'mechanic', 'discount', 'order', 'logo',)


class SubInline(admin.TabularInline):
    model = Sub
    extra = 1  # Number of extra forms to display initially
    fields = ('duration', 'prepayment_percentage', 'annual_interest_rate')  # Yangi maydon qo'shildi
    verbose_name = "Sub"
    verbose_name_plural = "Subs"


class InstallmentPlanInline(admin.TabularInline):
    model = InstallmentPlan
    extra = 1  # Number of extra forms to display initially
    fields = ('car',)  # Ensure the inline only has the necessary fields
    verbose_name = "Installment Plan"
    verbose_name_plural = "Installment Plans"
    show_change_link = True


@admin.register(InstallmentPlan)
class InstallmentPlanAdmin(admin.ModelAdmin):
    list_display = ('car',)
    list_filter = ('car',)
    inlines = [SubInline]