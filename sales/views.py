from django.db import models
from django.db.models import Count, Sum
from django.utils import timezone
from rest_framework import generics

from .filters import ClientStatisticsFilter
from .models import Employee, Client
from .serializers import EmployeeSerializer, ClientSerializer, AllEmployeeSerializer


class EmployeeStatisticsView(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'month': self.request.query_params.get('month'),
            'year': self.request.query_params.get('year')
        })
        return context


class AllEmployeesStatisticsView(generics.ListAPIView):
    serializer_class = AllEmployeeSerializer
    queryset = Employee.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'month': self.request.query_params.get('month'),
            'year': self.request.query_params.get('year')
        })
        return context


class ClientStatisticsView(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'month': self.request.query_params.get('month'),
            'year': self.request.query_params.get('year')
        })
        return context
