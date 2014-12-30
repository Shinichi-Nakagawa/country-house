from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from house.models import HouseRecord
from house.serializers import HouseRecordSerializer
from house.permissions import IsOwnerOrReadOnly


@api_view(('GET',))
@permission_classes((permissions.AllowAny, ))
def api_root(request, format=None):
    return Response({
        'records': reverse('record-list', request=request, format=format),
    })


class RecordList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    List all snippets, or create a new snippet.
    """
    queryset = HouseRecord.objects.all()
    serializer_class = HouseRecordSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
