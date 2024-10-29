from django.contrib import admin
from about.models import Top, Workers, Social, Services


@admin.register(Top)
class TopAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'image')


class SocialInline(admin.TabularInline):
    model = Social
    extra = 1


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    inlines = [SocialInline]
    list_display = ('name', 'position', 'created_at', 'updated_at')
    search_fields = ('name', 'position')
    fields = ('name_uz', 'name_ru', 'position_uz', 'position_ru', 'image',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    fields = ('title_uz', 'title_ru', 'description_uz', 'description_ru', 'svg_icon')
