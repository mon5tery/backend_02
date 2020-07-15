from rest_framework import serializers, permissions, status
from .models import Profile
from django.contrib.auth.models import User



def get_token(user):
		refresh = RefreshToken.for_user(user)
		return refresh.access_token

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	first_name = serializers.CharField(required=True)
	last_name = serializers.CharField(required=True)
	email = serializers.EmailField(required=True)
	access = serializers.CharField(read_only=True)

	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name', 'email', 'access', ]

		def create(self, validated_data):
			username = validated_data['username']
			password = validated_data['password']
			first_name = validated_data['first_name']
			last_name = validated_data['last_name']
			email = validated_data['email']

			new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)

			new_user.set_password(password)
			new_user.save()

			profile = Profile.objects.create(user=new_user)
			profile.save()

			validated_data["access"] = get_token(new_user)

			return validated_data


		def validate_email(self, email):
			user = User.objects.filter(email=email)
			if user:
				raise serializers.ValidationError("Email Exists.")
			return email


class ProfileSerializer(serializers.ModelSerializer):
	email = serializers.SerializerMethodField()

	class Meta:
		model = Profile
		fields = ['user', 'first_name', 'last_name', 'image', ]

	def get_username(self, obj):
		return "%s" % (obj.user.username)

	def get_name(self, obj):
		return '%s %s' % (obj.user.first_name, obj.user.last_name)

	# def get_email(self, obj):
	# 	return obj.user.email


class ProfileUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['image', 'first_name', 'last_name', 'email', ]



class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)
	access = serializers.CharField(allow_blank=True, read_only=True)

	def validate(self, data):
		my_username = data.get('username')
		my_password = data.get('password')

		try:
			user_obj = User.objects.get(username=my_username)
		except:
			raise serializers.ValidationError("This username does not exist")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination! Noob..")

	
		payload = RefreshToken.for_user(user_obj)
		token = str(payload.access_token)

		data["access"] = token

		return data










