from rest_framework import serializers

from .models import AddSections

class AddSectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddSections
        fields = ['id', 'newSection' ]