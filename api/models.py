from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Graph(models.Model):
    graph_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='graphs')
    graph_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.graph_name

class Asset(models.Model):
    ticker = models.CharField(max_length=10)
    company_name = models.CharField(max_length = 255)
    price_per_share = models.DecimalField(max_digits=15, decimal_places=2)
    div_yield = models.IntegerField()
    shares = models.DecimalField(max_digits=15, decimal_places=2)
    company_overview = models.TextField()
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='assets')

    def __str__(self):
        return self.ticker




