from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from juriidilisedjuured.models import Node
from juriidilisedjuured.serializers import NodeListSerializer, NodeRetrieveSerializer


class NodeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Node.objects.filter(parent_node__isnull=True)
        serializer = NodeListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Node.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = NodeRetrieveSerializer(user)

        return Response(serializer.data)
