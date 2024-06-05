from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
# PRebuilt vuiews to obtain access and refresh tokens. Once user created we can use toekn to sign them in
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Included urls from sequence_api
    path('entrez/', include('entrez_api.urls')),
    path('file/', include('file_upload_api.urls')),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    # path("api/", include("auth.urls")),
]