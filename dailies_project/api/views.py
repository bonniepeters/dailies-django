from django.contrib.auth.models import Day, Week
from rest_framework import viewsets
From .serializers import DaySerializer, WeekSerializer
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows days to be viewed or edited.
    """
    queryset = Day.objects.all().order_by('-date_joined')
    serializer_class = DaySerializer
class WeekViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weeks to be viewed or edited.
    """
    queryset = Week.objects.all()
    serializer_class = WeekSerializer