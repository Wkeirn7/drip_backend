from .models import Graph, Asset
from rest_framework import serializers

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            'id', 
            'ticker', 
            'company_name', 
            'price_per_share', 
            'div_yield', 
            'shares', 
            'company_overview', 
        ]


class GraphSerializer(serializers.ModelSerializer):
    assets = AssetSerializer(many=True, read_only=True)
    class Meta:
        model = Graph
        fields = [
            'id',
            'graph_name',
            'date_created',
            'reinvestment_period',
            'reinvestment_amount',
            'assets',
        ]
