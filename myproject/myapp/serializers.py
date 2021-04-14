from rest_framework import serializers
from myapp.models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('id',
                  'username',
                  'email',
                  'password')