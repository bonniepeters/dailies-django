from rest_framework import serializers

class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ['url', 'caption', 'numbered', 'day', 'week', 'water', 'work', 'connect', 'workout', 'music', 'code', 'mindful', 'read', 'learn', 'vitamins', 'timeSlots', 'outside', 'earth', 'food', 'oils', 'weight', 'awake', 'asleep']

class WeekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Week
        fields = ['url', 'caption', 'number']