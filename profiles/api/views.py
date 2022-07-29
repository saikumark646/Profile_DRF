from profiles.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from profiles.api.serializers import (ProfileAvatarSerializer,
                                      ProfileSerializer,
                                      ProfileStatusSerializer)

from profiles.api.pagination import SmallSetPagination
from profiles.models import Profile, ProfileStatus
from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response 

class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user.profile

# mixins.CreateModelMixin,
class ProfileViewSet(mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['city']        #  /?search=rome/
    pagination_class = SmallSetPagination


class ProfileStatusViewSet(ModelViewSet):
    
    serializer_class = ProfileStatusSerializer
    permission_classes =  [IsAuthenticated, IsOwnerOrReadOnly]

    def  get_queryset(self):                   #filtering system is added
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get('username',None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)     
            #/?username=admin
        return queryset
    

    def perform_create(self,serializer):
        serializer.save(user_profile = user_profile )
        user_profile = self.request.user.profile



# class ProfileDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_class = [IsAuthenticated]
