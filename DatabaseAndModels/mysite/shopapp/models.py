from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        """"""
        # db_table = 'user'
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=0), name='age_gte_0'),
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.SmallIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    user_comment = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(max_length=500, null=True)
    product = models.ManyToManyField(Product, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="user")
