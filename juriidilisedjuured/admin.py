from django.contrib import admin

from juriidilisedjuured.models import Node
from juriidilisedjuured.forms import NodeForm


class NodeAdmin(admin.ModelAdmin):
    form = NodeForm

admin.site.register(Node, NodeAdmin)