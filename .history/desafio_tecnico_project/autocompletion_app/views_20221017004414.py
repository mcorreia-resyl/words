from django.shortcuts import render
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Words
from .utils import trie
from .serializers import SearchSerializer


class SearchView(APIView):
    def get(self, request):
        q = self.request.GET.get('q', '')
        # results = trie.query(q)
        results = Words.objects.filter(Q(word__icontains=q))[:100]
        serializer = SearchSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
