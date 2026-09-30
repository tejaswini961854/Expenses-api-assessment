from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from .models import ExpenseRecord, ExpenseCategory
from .serializers import ExpenseSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions. IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'payment_method']
    search_fields = ['description']

    def get_queryset(self):
        return ExpenseRecord.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def expense_summary(request):
    user_expenses = ExpenseRecord.objects.filter(owner=request.user)

    total_amount = user_expenses.aggregate(total=Sum('amount'))['total'] or 0

    category_totals = user_expenses.values('category__name').annotate(
        category_sum=Sum('amount')
    ).order_by('-category_sum')

    category_wise_data = {
        item['category__name'] if item['category__name'] else 'Uncategorized': item['category_sum']
        for item in category_totals
    }

    return Response({
        "total_expense": total_amount,
        "category_wise": category_wise_data
    })



    