from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentAPIView

router = DefaultRouter()
# router.register('payment', PaymentViewSet, base_name="payment")


app_name = 'rest'
urlpatterns = [
    path('payment/<slug:identity_number>/<slug:account_number>/', PaymentAPIView.as_view()),
]
