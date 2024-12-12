from drf_spectacular.views import SpectacularAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication,
)

from drf_spectacular.utils import extend_schema


@extend_schema(exclude=True)
class CustomSpectacularAPIView(SpectacularAPIView):
    """
    A custom view for generating OpenAPI schema using drf-spectacular.

    This class extends `SpectacularAPIView` provided by drf-spectacular
    to customize the permissions and authentication classes used by the view.

    Attributes:
        permission_classes (list of classes): [IsAdminUser]
            A list of permission classes applied to this viewset.
            Only users with the specified permissions
            will be able to access the associated endpoints. In this case,
            only users with admin privileges are allowed.
        authentication_classes (list of classes): [JWTAuthentication,\
            SessionAuthentication]
            A list of authentication classes used to verify
            the identity of users making requests
            to the endpoints. In this case, the endpoints can be accessed
            using either JWT Authentication or Session Authentication.
    """

    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
