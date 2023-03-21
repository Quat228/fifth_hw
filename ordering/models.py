from django.db import models


class User(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=20)
    card_number = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")

    def save(self, *args, **kwargs):
        if type(self.card_number) != int:
            self.card_number = int(self.card_number.replace(" ", ""))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="worker")

    def __str__(self):
        return f"Worker {self.name}, pos: {self.position}"


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField()
    #  ManyToManyField не нужен, так как при заказе он учитывается

    def __str__(self):
        return f"Food {self.name}"


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="orders")
    ingredients = models.ManyToManyField(Ingredient, related_name="orders", null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="orders")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="orders")
    order_date_time = models.DateTimeField(auto_now=True)

    def get_price(self):
        return self.food.start_price + sum([x.extra_price for x in self.ingredients.all()])

    def __str__(self):
        return f"Order: {self.food}, {[x for x in self.ingredients.all()]}, {self.client}, {self.worker}, {self.order_date_time}"
