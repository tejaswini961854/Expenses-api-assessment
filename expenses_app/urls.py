from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ExpenseViewSet, UserRegistrationView, expense_summary

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense') 

urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/expenses/summary/', expense_summary, name='expense-summary'), 
    path('api/', include(router.urls)),
]