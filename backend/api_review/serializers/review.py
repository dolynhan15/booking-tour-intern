from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from ..models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'tour', 'content']

    def validate(self, attrs):
        user = attrs.get('user', '')
        tour = attrs.get('tour', '')

        if not user:
            raise AuthenticationFailed('User not empty, try again')
        elif not tour:
            raise AuthenticationFailed('Tour not empty, try again')
