from rest_framework import serializers

from juriidilisedjuured.models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', 'help_text')


class NodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', 'help_text')


class NodeRetrieveSerializer(serializers.ModelSerializer):
    parent_node = NodeSerializer()
    child_nodes = NodeSerializer(many=True)

    class Meta:
        model = Node
        fields = ('id', 'name', 'help_text', 'parent_node', 'child_nodes')
