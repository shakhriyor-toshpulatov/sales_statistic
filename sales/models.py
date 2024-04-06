from django.db import models


class Employee(models.Model):
    """Сотрудник"""
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.full_name


class Client(models.Model):
    """Клиент"""
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.full_name


class Product(models.Model):
    """Продукты"""
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Заказ"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'Client: {self.client} -> Employee {self.employee} | Date {self.date}'
