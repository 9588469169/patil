from rest_framework import serializers
from myapp.models import Product,User

class ProduceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('password', 'email', 'first_name', 'last_name', 'mobile')
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)