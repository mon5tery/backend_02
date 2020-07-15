from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer, UserCreateSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser



class UserCreateView(CreateAPIView):
	serializer_class = UserCreateSerializer

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)


class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request):
		my_data = request.data
		serializer = UserLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class ProfileDetails(RetrieveAPIView):
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()
	permission_classes = [IsAuthenticated]

	def get_object(self):
		# user = self.request.user
		# queryset = self.queryset.get(user=user)
		# return queryset

		return self.request.user.profile