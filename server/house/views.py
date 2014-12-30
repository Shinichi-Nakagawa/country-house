from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from house.models import HouseRecord
from house.serializers import HouseRecordSerializer, UserSerializer
from house.permissions import IsOwnerOrReadOnly


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

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer