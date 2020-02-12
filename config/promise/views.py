from .models import Promise
from .serializers import PromiseDetailSerializer, PromiseListSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly



class PromiseCreateView(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    serializer_class = PromiseDetailSerializer
    queryset = Promise.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PromiseListView(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PromiseListSerializer
    queryset = Promise.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PromiseDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PromiseDetailSerializer
    queryset = Promise.objects.all()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer