from rest_framework import viewsets
from .models import User , Event
from .serializers import UserSerializer , EventSerializer
from rest_framework import generics

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserView(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        users = self.queryset.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):

        try:
            return self.queryset.get(pk=pk)
        except User.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)


    def assign_admin_role(self, request, pk):
        user= self.get_object(pk)
        user.role = 'ROLE_ADMIN'
        user.save()
        return Response(status=status.HTTP_200_OK)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer




class EventView(viewsets.ViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):
        events = self.queryset.all()
        serializer = self.serializer_class(events, many=True)
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
        

    # def append_new_attendee




