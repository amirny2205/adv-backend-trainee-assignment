from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView

from ads.models import Ad
from ads.serializers import AdSerializer


# Create your views here.


class AdList(APIView):
    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data)


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

