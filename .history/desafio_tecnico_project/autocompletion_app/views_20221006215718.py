from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SearchSerializer
from .models import Words

class SearchView(APIView):
    def get(self,request):
        q = self.request.GET.get('q','')
        results = Words.objects.filter(Q(word__icontains=q))
        serializer = SearchSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllWordsView(APIView):
    def get(self,request):
        results = Words.objects.all()
        serializer = SearchSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
