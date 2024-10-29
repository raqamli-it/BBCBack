from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


from credit_conditions.models import Info


@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
