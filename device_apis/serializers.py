from rest_framework import serializers
from device_apis.models import Devices, DeviceSold, User


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'


    def create(self, validated_data):
        device = Devices.objects.create(**validated_data)
        device.save()
        return device


class DeviceSoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceSold
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]



    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class UserLoginTokenSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=100)
        password = serializers.CharField(max_length=100)