from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny


from events.permissions import IsAuthenticatedAndHasRoleAdmin , IsAuthenticatedAndHasRoleUser , IsEventOwner
from .models import User , Event
from .serializers import UserSerializer , EventSerializer
from rest_framework import generics

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import permissions


from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone
from django.db.models import Q

class UserView(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow anyone to create a new user


    def list(self, request):
        print(f"User: {request.user}")
        print(f"Is authenticated: {request.user.is_authenticated}")
        if hasattr(request.user, 'role'):
            print(f"User role: {request.user.role}")
        else:
            print("User has no role attribute")

        if IsAuthenticatedAndHasRoleAdmin().has_permission(request, self):
            users = self.queryset.all()
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)


    def signup(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def destroy(self, request, pk=None):
        self.check_permissions(request)  # This will check the default permissions
        if not IsAuthenticatedAndHasRoleAdmin().has_permission(request, self):
            return Response(status=status.HTTP_403_FORBIDDEN)
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    def get_object(self, pk):

        try:
            return self.queryset.get(pk=pk)
        except User.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)




    def assign_admin_role(self, request, pk=None):
        # Check permissions manually
        permission = IsAuthenticatedAndHasRoleAdmin()
        if not permission.has_permission(request, self):
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        try:
            user = self.queryset.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.role = 'ROLE_ADMIN'
        user.save()
        return Response({"message": f"Admin role assigned to user {user.username}"}, status=status.HTTP_200_OK)


from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'start_date', 'end_date', 'location', 'organizer']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['start_date', 'end_date', 'capacity']


    def list(self, request):
        """
        List all events.
        
        This endpoint supports:
        - Filtering by: title, start_date, end_date, location, organizer
        - Searching in: title, description, location
        - Ordering by: start_date, end_date, capacity
        
        Example usage:
        /api/event/getEventList/?title=Party&location=New York&search=concert&ordering=-start_date
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        event = self.get_object(pk)
        serializer = self.serializer_class(event)
        return Response(serializer.data)
    def update(self, request, pk=None):
        event = self.get_object(pk)
        serializer = self.serializer_class(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
    
        try:
            return self.queryset.get(pk=pk)
        except Event.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        

    def join_event(self, request, pk=None):
        if not IsAuthenticatedAndHasRoleUser().has_permission(request, self):
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        event = self.get_object(pk)
        user = request.user

        if event.attendees.filter(id=user.id).exists():
            return Response({"message": "You are already registered for this event."}, status=status.HTTP_400_BAD_REQUEST)

        if event.waitlist.filter(id=user.id).exists():
            return Response({"message": "You are already on the waitlist for this event."}, status=status.HTTP_400_BAD_REQUEST)

        success, message = event.add_attendee(user)
        if success:
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_202_ACCEPTED)

    def get_waitlist(self, request, pk=None):
        if not IsAuthenticatedAndHasRoleUser().has_permission(request, self):
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        event = self.get_object(pk)
        waitlist = event.waitlist.all()
        serializer = UserSerializer(waitlist, many=True)
        return Response(serializer.data)

    def manage_capacity(self, request, pk=None):
        if not IsEventOwner().has_permission(request, self):
            return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        event = self.get_object(pk)
        new_capacity = request.data.get('capacity')

        if new_capacity is None:
            return Response({"error": "New capacity not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            new_capacity = int(new_capacity)
        except ValueError:
            return Response({"error": "Invalid capacity value"}, status=status.HTTP_400_BAD_REQUEST)

        if new_capacity < event.actual_attendees:
            return Response({"error": "New capacity cannot be less than current attendees"}, status=status.HTTP_400_BAD_REQUEST)

        event.capacity = new_capacity
        event.save()

        # If capacity increased, move users from waitlist to attendees
        while event.actual_attendees < event.capacity and event.waitlist.exists():
            user_to_move = event.waitlist.first()
            event.waitlist.remove(user_to_move)
            event.attendees.add(user_to_move)
            event.actual_attendees += 1

        event.save()

        return Response({"message": f"Capacity updated to {new_capacity}"}, status=status.HTTP_200_OK)

    def upcoming_events(self, request):
        now = timezone.now()
        queryset = self.queryset.filter(start_date__gt=now)

        search = request.query_params.get('search')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(location__icontains=search))

        if start_date:
            queryset = queryset.filter(start_date__gte=start_date)

        if end_date:
            queryset = queryset.filter(start_date__lte=end_date)

        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




