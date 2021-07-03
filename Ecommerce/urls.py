from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers

route = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('ApiApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
