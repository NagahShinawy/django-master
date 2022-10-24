from rest_framework import serializers
from ..models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("pk", "title", "is_completed", "url", "order")
