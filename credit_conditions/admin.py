from django.contrib import admin

from credit_conditions.models import Info


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'file',)
