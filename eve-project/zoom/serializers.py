from rest_framework import serializers, fields

from .models import Zoom


class ZoomSerializer(serializers.ModelSerializer):
    start_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    end_date = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
            model = Zoom
            fields = ('id', 'title', 'start_date', 'end_date','description', 'zoom_url', 'password', 'zoom_id')
