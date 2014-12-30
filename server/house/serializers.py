#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

from django.contrib.auth.models import User
from rest_framework import serializers
from house.models import HouseRecord


class HouseRecordSerializer(serializers.Serializer):
    code = serializers.CharField(required=True, max_length=100)
    temperature = serializers.FloatField()
    memo = serializers.CharField(required=False, max_length=255)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return HouseRecord.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.memo = validated_data.get('memo', instance.memo)
        instance.save()
        return instance

    class Meta:
        model = HouseRecord
        fields = ('code', 'temperature', 'memo', 'owner')


class UserSerializer(serializers.ModelSerializer):
    records = serializers.PrimaryKeyRelatedField(many=True, queryset=HouseRecord.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'records')