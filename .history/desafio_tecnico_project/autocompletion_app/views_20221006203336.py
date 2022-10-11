from django.shortcuts import render
from serializers import SearchSerializer
from models import Words
class SearchView(APIView):
    def get(self,request):
        q = self.request.GET.get('q')
        results = Words.objects.filter(Q)
