from rest_framework import serializers
from rental.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ["id", "vehicle", "user", "user_username", "rating", "comment", "created_at"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        # Asignamos automáticamente el usuario autenticado
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
