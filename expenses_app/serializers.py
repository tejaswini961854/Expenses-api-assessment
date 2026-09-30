from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ExpenseRecord, ExpenseCategory

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name']
class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = ExpenseRecord
        fields =['id', 'amount', 'description', 'category', 'category_name',
                 'expense_date', 'payment_method', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be strictly greater than 0.")
        return value