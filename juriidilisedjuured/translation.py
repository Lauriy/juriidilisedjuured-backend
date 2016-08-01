from modeltranslation.translator import translator, TranslationOptions

from juriidilisedjuured.models import Node


class NodeTranslationOptions(TranslationOptions):
    fields = ('name', 'help_text',)


translator.register(Node, NodeTranslationOptions)
