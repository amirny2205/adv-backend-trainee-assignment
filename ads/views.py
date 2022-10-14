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




class AdDetail(generics.RetrieveAPIView):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer




class AdCreate(generics.CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return Response(serializer.data['id'], status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     print('using local perform_create')
    #     request = serializer.context['request']
    #     if 'photos' in request.data and len(request.data['photos'])>0:
    #         main_photo = request.data['photos'][0]
    #         serializer.save(main_photo=main_photo)
    #     serializer.save()
