from django.db import models


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    sampleURL = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    url = models.URLField(max_length=200, null=True)
    paidDate = models.DateTimeField(null=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    completed = models.BooleanField(default=False, null=True)
    paid = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.id)


class OrderProxy(Order):
    class Meta:
        proxy = True
        verbose_name = 'Pending Order'
        verbose_name_plural = 'Pending Orders'


class Wallet(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.user.username + ': ' + str(self.balance)
