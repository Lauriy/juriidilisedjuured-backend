from dal import autocomplete
from django import forms

from juriidilisedjuured.models import Node


class NodeForm(forms.ModelForm):
    parent_node = forms.ModelChoiceField(
        queryset=Node.objects.all(),
        widget=autocomplete.ModelSelect2(url='node-autocomplete'),
        required=False
    )

    class Meta:
        model = Node
        fields = '__all__'
