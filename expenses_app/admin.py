from django.contrib import admin
from .models import ExpenseCategory, ExpenseRecord

admin.site.register(ExpenseCategory)
admin.site.register(ExpenseRecord)