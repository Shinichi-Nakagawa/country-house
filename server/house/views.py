from house.models import HouseRecord
from house.serializers import HouseRecordSerializer
from rest_framework import mixins
from rest_framework import generics


class RecordList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = HouseRecord.objects.all()
    serializer_class = HouseRecordSerializer
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)