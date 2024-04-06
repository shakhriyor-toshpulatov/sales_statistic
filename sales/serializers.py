from django.db import models
from rest_framework import serializers
from .models import Employee, Client, Product, Order


class RoundingDecimalField(serializers.DecimalField):
    """Используется для автоматического округления десятичных дробей до принятого в модели значения."""

    def validate_precision(self, value):
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    num_clients = serializers.SerializerMethodField()
    num_products_sold = serializers.SerializerMethodField()
    total_sales = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'num_clients', 'num_products_sold', 'total_sales']

    def get_num_clients(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.values('client').distinct().count()

    def get_num_products_sold(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.aggregate(total_products=models.Sum('products__quantity'))['total_products']

    def get_total_sales(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.aggregate(total_sales=models.Sum('price'))['total_sales']


class AllEmployeeSerializer(serializers.ModelSerializer):
    num_clients = serializers.SerializerMethodField()
    num_products_sold = serializers.SerializerMethodField()
    total_sales = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'num_clients', 'num_products_sold', 'total_sales']

    def get_num_clients(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.values('client').distinct().count()

    def get_num_products_sold(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.aggregate(total_products=models.Sum('products__quantity'))['total_products']

    def get_total_sales(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.aggregate(total_sales=models.Sum('price'))['total_sales']


class ClientSerializer(serializers.ModelSerializer):
    num_products = serializers.SerializerMethodField()
    total_sales = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'full_name', 'num_products', 'total_sales']

    def get_num_products(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.aggregate(total_products=models.Sum('products__quantity'))['total_products']

    def get_total_sales(self, obj):
        month = self.context.get('month')
        year = self.context.get('year')
        queryset = obj.order_set.filter(date__month=month, date__year=year)
        return queryset.aggregate(total_sales=models.Sum('price'))['total_sales']
