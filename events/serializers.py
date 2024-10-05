from rest_framework import serializers
from .models import User, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


