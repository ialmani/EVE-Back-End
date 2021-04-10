from rest_framework import serializers

from .models import Zoom


class ZoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zoom
        fields = ('id', 'title', 'start_time', 'date','description', 'zoom_url', 'password', 'zoom_id')
