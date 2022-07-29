from django.urls import path,include

from profiles.api.views import ProfileViewSet, AvatarUpdateView,ProfileStatusViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profile",ProfileViewSet) 
# this rounter will genarate end points automatically
router.register(r"status",ProfileStatusViewSet,basename = 'status')

urlpatterns = [
    path('',include(router.urls)),
    path('avatar/',AvatarUpdateView.as_view(),name = 'AvatarUpdateView')
]





#below is the process to manually create endpoints for the viewset class
# profile_list = ProfileViewSet.as_view({'get':'list'})
# profile_detail = ProfileViewSet.as_view({'get':'retrieve'})
# #profile_destroy = ProfileViewSet.as_view({'get':'destroy'})
# urlpatterns = [
#     path('profile/',profile_list,name = 'profile_list'),
#     path('profile/<int:pk>/',profile_detail,name = 'profile_detail'),
    
#     path('avatar/',AvatarUpdateView.as_view(),name = 'AvatarUpdateView')
# ] 



