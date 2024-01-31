from rest_framework import viewsets
from .models import Query
from .serializers import QuerySerializer

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer