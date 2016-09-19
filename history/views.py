from django.shortcuts import render
from history.models import LogHistory
from history.serializers import HistorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from git import Repo

class historyList(APIView):
    def get(self,request):
        repo = Repo('/home/sandra/trotamundia/sandra/trotamundiaHistory')
        print repo.head.commit
        print repo.head.commit.author.name
        queryset = LogHistory.objects.all()
        return Response({'histories':queryset})