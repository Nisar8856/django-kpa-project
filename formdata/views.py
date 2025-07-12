from rest_framework import generics
from .models import FormData
from .serializers import FormDataSerializer

class FormDataCreate(generics.CreateAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer

class FormDataRetrieve(generics.RetrieveAPIView):
    queryset = FormData.objects.all()
    serializer_class = FormDataSerializer
