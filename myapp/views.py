from rest_framework import generics
from .models import Designer
from .serializers import DesignerSerializer

class DesignerListCreateView(generics.ListCreateAPIView):
    queryset = Designer.objects.all()
    serializer_class = DesignerSerializer
