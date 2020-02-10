from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class PromiseDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Promise
        fields = '__all__'
        # fields = ('id, owner', 'name', 'dline', 'desc', 'create_time', )



class PromiseListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Promise
        fields = '__all__'
        # fields = ('id, owner', 'name', 'dline', 'desc', 'create_time', )

    #
    # name = models.CharField(max_length=255, blank=False)
    # dline = models.CharField(max_length=20, blank=False)
    # desc = models.CharField(max_length=255, blank=False)
    # create_time = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey('auth.User', related_name='promise', on_delete=models.CASCADE)

class UserSerializer(serializers.ModelSerializer):
    promise = serializers.PrimaryKeyRelatedField(many=True, queryset=Promise.objects.all())

    class Meta:
        model = User
        print(model)
        fields = ('id', 'username', 'promise') # from model in line owner

