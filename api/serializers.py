from rest_framework import serializers
from main.models import CV


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = [
            'id',
            'first_name',
            'last_name',
            'bio',
            'skills',
            'projects',
            'contacts'
        ]
