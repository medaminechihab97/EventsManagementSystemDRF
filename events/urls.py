from django.urls import path
from .views import   UserView , EventView
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomTokenObtainPairView





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
    path('user/', UserView.as_view({'get': 'list'}), name='newUser-list'),
    path('signup/', UserView.as_view({'post': 'signup'}), name='newUser-create'),
    path('user/<int:pk>/', UserView.as_view({'get': 'retrieve'}), name='newUser-detail'),
    path('user/<int:pk>/update/', UserView.as_view({'put': 'update'}), name='newUser-update'),
    path('user/<int:pk>/delete/', UserView.as_view({'delete': 'destroy'}), name='newUser-delete'),
    path('event/getEventList/', EventView.as_view({'get': 'list'}), name='event-list'),
    path('event/createNewEvent/', EventView.as_view({'post': 'create'}), name='event-create'),
    path('event/getEventById/<int:pk>/', EventView.as_view({'get': 'retrieve'}), name='event-detail'),
    path('event/updateEvent/<int:pk>', EventView.as_view({'put': 'update'}), name='event-update'),
    path('event/deleteEvent/<int:pk>', EventView.as_view({'delete': 'destroy'}), name='event-delete'),
    path('signin/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/<int:pk>/assign_admin_role/', UserView.as_view({'post': 'assign_admin_role'}), name='assign-admin-role'),
    path('events/<int:pk>/join/', EventView.as_view({'post': 'join_event'}), name='join-event'),
    path('events/<int:pk>/waitlist/', EventView.as_view({'get': 'get_waitlist'}), name='event-waitlist'),
    path('events/<int:pk>/manage-capacity/', EventView.as_view({'post': 'manage_capacity'}), name='manage-event-capacity'),
    path('events/upcoming/', EventView.as_view({'get': 'upcoming_events'}), name='upcoming-events'),





]