from django.shortcuts import render
from django.db.models import Q
from rest_framework import status, R
from serializers import SearchSerializer
from models import Words

class SearchView(APIView):
    def get(self,request):
        q = self.request.GET.get('q')
        results = Words.objects.filter(Q(word__icontains=q))
        serializer = SearchSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
