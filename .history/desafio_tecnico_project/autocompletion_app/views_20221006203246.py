from django.shortcuts import render
from serializers import SearchSerializer
class SearchView(APIView):
    def get(self,request):
        q = self.request.GET.get('q')
