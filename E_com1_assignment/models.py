from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.line_1}, {self.line_2}"


class Order(models.Model):
    user_name = models.ForeignKey(User, related_name="Order", on_delete=models.CASCADE)
    order_date = models.DateTimeField()

    def __str__(self):
        return self.user_name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class OrderProducts(models.Model):
    order_id = models.ForeignKey(
        Order, related_name="OrderProducts", on_delete=models.CASCADE
    )
    product_id = models.ForeignKey(
        Product, related_name="OrderProducts", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price_at_ordered = models.IntegerField()


