from django.urls import path
from .views import AssetRetrieveUpdateDestroy, GraphViewList, GraphRetrieveUpdateDestroy, AssetCreate

urlpatterns = [
    path('graphs/', GraphViewList.as_view(), name='graphs'),
    path('graphs/<int:id>/', GraphRetrieveUpdateDestroy.as_view(), name='graphdetail'),
    path('graphs/<int:graph_id>/addasset/', AssetCreate.as_view(), name='addasset'),
    path('graphs/<int:graph_id>/<int:asset_id>/', AssetRetrieveUpdateDestroy.as_view(), name='assetretrieve'),
]
