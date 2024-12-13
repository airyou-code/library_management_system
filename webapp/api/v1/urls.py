from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularRedocView
)
from ..views import CustomSpectacularAPIView

app_name = "v1"

urlpatterns = [
    path('', include("library.api.v1.urls")),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'token/refresh/', TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        '',
        SpectacularSwaggerView.as_view(url_name="api:v1:schema"),
        name='swagger-ui'
    ),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name="api:v1:schema"),
        name='redoc'
    ),
    path('schema/', CustomSpectacularAPIView.as_view(api_version="v1"), name='schema'),
]
