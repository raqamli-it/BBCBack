from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


from catalog.models import Logo, Car


@register(Logo)
class LogoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'color',)
