from django.urls import path
from .views import  EventList ,  UserView , EventView
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions




schema_view = get_schema_view(
    openapi.Info(
        title="Events Management System API",
        default_version='v1',
        description="API for managing events in the Events Management System",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
) 


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('newUser/', UserView.as_view({'get': 'list'}), name='newUser-list'),
    path('newUser/create/', UserView.as_view({'post': 'create'}), name='newUser-create'),
    path('newUser/<int:pk>/', UserView.as_view({'get': 'retrieve'}), name='newUser-detail'),
    path('newUser/<int:pk>/update/', UserView.as_view({'put': 'update'}), name='newUser-update'),
    path('newUser/<int:pk>/delete/', UserView.as_view({'delete': 'destroy'}), name='newUser-delete'),
    path('event/getEventList/', EventView.as_view({'get': 'list'}), name='event-list'),
    path('event/createNewEvent/', EventView.as_view({'post': 'create'}), name='event-create'),
    path('event/getEventById/<int:pk>/', EventView.as_view({'get': 'retrieve'}), name='event-detail'),
    path('event/updateEvent/<int:pk>', EventView.as_view({'put': 'update'}), name='event-update'),
    path('event/deleteEvent/<int:pk>', EventView.as_view({'delete': 'destroy'}), name='event-delete'),



]