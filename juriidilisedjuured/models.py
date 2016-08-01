from django.db import models
from django.utils.translation import ugettext_lazy as _


class Node(models.Model):
    parent_node = models.ForeignKey('self', blank=True, null=True, related_name='child_nodes',
                                    verbose_name=_('parent node'))
    name = models.CharField(_('name'), max_length=255)
    help_text = models.CharField(_('help text'), max_length=255, blank=True, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    def __str__(self):
        return self.name