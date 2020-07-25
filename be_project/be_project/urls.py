from django.contrib import admin
from django.urls import path
from be_app.views import UserCreateView, ProfileDetails, PostView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usercreate/', UserCreateView.as_view(), name='usercreate'),
    path('profile/', ProfileDetails.as_view(), name='profile'),
    path('api/token/', TokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('post/', PostView.as_view(), name='post')
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)