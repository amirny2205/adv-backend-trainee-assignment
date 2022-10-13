import json

from django.conf import settings
from django.shortcuts import render
from rest_framework import status, generics, filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ads.models import Ad
from ads.serializers import AdSerializer
from rest_framework.pagination import PageNumberPagination


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class AdList(generics.ListAPIView):
    queryset = Ad.objects.all()
    pagination_class = BasicPagination
    serializer_class = AdSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'creation_date']



class AdDetail(APIView):
    def get(self, request, pk):
        ad = get_object_or_404(Ad.objects.all(), id=pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data)



class AdCreate(generics.CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    # def perform_create(self, serializer):
    #     request = serializer.context['request']
    #     main_photo = json.loads(request.data['photos'])[0]
    #     serializer.save(main_photo=main_photo)
