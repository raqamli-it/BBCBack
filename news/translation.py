from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


from news.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
