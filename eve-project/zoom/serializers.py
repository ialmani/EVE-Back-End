from rest_framework import serializers

from .models import Zoom


class ZoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zoom
        fields = ('id', 'title', 'date_time', 'zoom_url', 'description', 'password')
