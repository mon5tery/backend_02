from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import Profile, Post, PostImage
from .serializers import ProfileSerializer, UserCreateSerializer, UserLoginSerializer, PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import permissions
from .models import Profile as User



class UserCreateView(CreateAPIView):
	serializer_class = UserCreateSerializer

class ProfileDetails(RetrieveAPIView):
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()
	permission_classes = [IsAuthenticated]

	def get_object(self):
		user = self.request.user
		queryset = self.queryset.get(user=user)
		return queryset

class PostView(CreateAPIView):
	serializer_class = PostSerializer

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)













