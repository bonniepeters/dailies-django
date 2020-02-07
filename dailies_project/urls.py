from django.urls import include, path
from rest_framework import routers
from rapidapipractice.api import views
router = routers.DefaultRouter()
router.register(r'days', views.DayViewSet)
router.register(r'weeks', views.WeekViewSet)
# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]