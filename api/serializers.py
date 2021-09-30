from django.db.migrations import serializer

from .models import Statistic


class StatisticSerializer(serializer.ModelFieldSerializer):

    class Meta:
        model = Statistic
        fields = '__all__'

    def create(self, validated_data):
        return Statistic.objects.create(**validated_data)




