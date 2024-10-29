from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


from about.models import Top, Workers, Services


@register(Top)
class TopTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Workers)
class WorkersTranslationOptions(TranslationOptions):
    fields = ('name', 'position',)


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
