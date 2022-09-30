from django.urls import path
from applications.openpay_integration.views import CreateChargeView

urlpatterns = [
    path('donate/', CreateChargeView.as_view(), name='donate'),
]