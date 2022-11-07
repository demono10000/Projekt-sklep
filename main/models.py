from django.db import models


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    url = models.URLField(max_length=200)
    date = models.DateField()
    price = models.FloatField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Wallet(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.user.username + ': ' + str(self.balance)
