from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


from slider.models import Slider


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
