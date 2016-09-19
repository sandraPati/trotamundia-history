from rest_framework_mongoengine.serializers import DocumentSerializer
from history.models import LogHistory
from rest_framework import serializers

class HistorySerializer(DocumentSerializer):
    class Meta:
        model = LogHistory
        fields = ('description')