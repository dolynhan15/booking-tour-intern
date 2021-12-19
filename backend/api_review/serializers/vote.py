from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from ..models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'review', 'status']

    def validate(self, attrs):
        user = attrs.get('user', '')
        review = attrs.get('review', '')

        if not user:
            raise AuthenticationFailed('User not empty, try again')
        elif not review:
            raise AuthenticationFailed('Review not empty, try again')
