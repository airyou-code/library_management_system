from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet, LoanViewSet

router = DefaultRouter()

# Removing the automatic creation of the root path
router.include_root_view = False

router.register(r'books', BookViewSet, basename='book')
router.register(r'loans', LoanViewSet, basename='loan')

urlpatterns = [
    path('', include(router.urls)),
]
