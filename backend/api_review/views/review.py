from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions

from ..models import Review
from ..serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ViewSet):
    queryset = Review.objects.all()
    def list(self, request):
        serializer = ReviewSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ReviewSerializer(item)
        return Response(serializer.data)

    @permission_classes([permissions.IsAuthenticated])
    def create(self, request):
        pass

    @permission_classes([permissions.IsAuthenticated])
    def update(self, request, pk=None):
        pass

    @permission_classes([permissions.IsAuthenticated])
    def partial_update(self, request, pk=None):
        pass

    @permission_classes([permissions.IsAuthenticated])
    def destroy(self, request, pk=None):
        pass