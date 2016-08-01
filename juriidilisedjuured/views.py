from dal import autocomplete
from django.shortcuts import render

from juriidilisedjuured.models import Node


class NodeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Node.objects.none()

        qs = Node.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
