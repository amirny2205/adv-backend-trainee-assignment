from django.conf import settings
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ads.models import Ad
from ads.serializers import AdSerializer
from rest_framework.pagination import PageNumberPagination


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'



class AdList(APIView):
    pagination_class = BasicPagination
    serializer_class = AdSerializer
    def get(self, request, format=None, *args, **kwargs):
        objs = Ad.objects.all()

        self._paginator = BasicPagination()
        self._paginator.paginate_queryset(objs, request, view=self)
        page = self._paginator.paginate_queryset(objs, request, view=self)
        if page is not None:
            serializer = self._paginator.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)




class AdDetail(APIView):
    def get(self, request, pk):
        ad = get_object_or_404(Ad.objects.all(), id=pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data)



class AdCreate(APIView):
    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

