from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer, UserCreateSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import permissions
from .models import Profile as User


class UserCreateView(CreateAPIView):
	serializer_class = UserCreateSerializer
	# permission_classes = (permissions.AllowAny,)

	# def post(self, request, *args, **kwargs):
	# 	serialized_user = UserCreateSerializer(data=request.data)
	# 	if serialized_user.is_valid():
	# 		User.objects.create_user(
	# 			serialized_user.initial_data['email'],
	# 			serialized_user.initial_data['password']
	# 		)

	# 		tokens = MyTokenObtainPairSerializer(request.data).validate(request.data)
	# 		return Response(tokens, status=status.HTTP_201_CREATED)
	# 	else:
	# 		return Response(serialized_user._errors, status=status.HTTP_400_BAD_REQUEST)

	# def perform_create(self, serializer):
	# 	serializer.save(user=self.request.user)


# class UserLoginAPIView(APIView):
# 	serializer_class = UserLoginSerializer

# 	def post(self, request):
# 		my_data = request.data
# 		serializer = UserLoginSerializer(data=my_data)
# 		if serializer.is_valid(raise_exception=True):
# 			valid_data = serializer.data
# 			return Response(valid_data, status=HTTP_200_OK)
# 		return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class ProfileDetails(RetrieveAPIView):
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()
	permission_classes = [IsAuthenticated]

	def get_object(self):
		# user = self.request.user
		# queryset = self.queryset.get(user=user)
		# return queryset

		return self.request.user