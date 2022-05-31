from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import AssetSerializer, GraphSerializer
from .models import Graph, Asset
from .exceptions import InvalidUserException

# Create your views here.
class GraphViewList(generics.ListCreateAPIView):
    serializer_class = GraphSerializer

    def get_queryset(self):
        return Graph.objects.filter(graph_owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(graph_owner=self.request.user)

class GraphRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GraphSerializer
    lookup_field = 'id'

    def get_queryset(self):
        graph = Graph.objects.filter(graph_owner=self.request.user)
        return graph

class AssetCreate(generics.CreateAPIView):
    serializer_class = AssetSerializer
    lookup_url_kwarg = 'graph_id'

    def perform_create(self, serializer):
        graph_id = self.kwargs.get(self.lookup_url_kwarg)
        graph_to_save_to = Graph.objects.get(id=graph_id)
        if self.request.user == graph_to_save_to.graph_owner:
            return serializer.save(graph=graph_to_save_to)
        else:
            raise InvalidUserException(detail={"Failure": "Invalid User"}, status_code=status.HTTP_403_FORBIDDEN)

class AssetRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    lookup_field = 'asset_id'

    def get_object(self):
        asset = Asset.objects.get(id=self.kwargs.get(self.lookup_field))
        asset_graph_id = asset.graph.id
        graph = Graph.objects.get(id=asset_graph_id)
        asset_user = graph.graph_owner
        if self.request.user == asset_user:
            return asset
        else:
            raise InvalidUserException(detail={"Failure": "Invalid User"}, status_code=status.HTTP_403_FORBIDDEN)
