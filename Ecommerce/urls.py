from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from ApiApp.views import RegistrationAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ApiApp.urls')),
    #path('api/v1/auth/auth-token', obtain_auth_token, name='obtain-auth-token')
    path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
