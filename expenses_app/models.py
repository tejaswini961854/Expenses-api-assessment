from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class ExpenseRecord(models.Model):
    PAYMENT_CHOICES = [
        ('CASH', 'cash'),
        ('CARD', 'card'),
        ('UPI', 'UPI'),
        ('NETBANKING', 'Net Banking')
    ]


    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    expense_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner.username} - {self.amount} - {self.description}"
    