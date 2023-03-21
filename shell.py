from ordering.models import User, Client, Worker, Ingredient, Food, Order

u1 = User.objects.create(email=" nikname21@gmail.com", password="defender42")
c1 = Client.objects.create(name="Азат Соколов", card_number="4147 5657 9878 9009", user=u1)

u2 = User.objects.create(email="altywa1998@gmail.com", password="nono34")
w1 = Worker.objects.create(name="Алтынай Алиева", position="Оператор кассы", user=u2)

f1 = Food.objects.create(name="Shawarma", start_price=50)
f2 = Food.objects.create(name="Hamburger", start_price=25)

i1 = Ingredient.objects.create(name="Cheese", extra_price=10)
i2 = Ingredient.objects.create(name="Chicken", extra_price=70)
i3 = Ingredient.objects.create(name="Beef", extra_price=80)
i4 = Ingredient.objects.create(name="Salad", extra_price=15)
i5 = Ingredient.objects.create(name="French_fries", extra_price=15)

o1 = Order.objects.create(food=f1, client=c1, worker=w1)
o1.ingredients.set([i1, i3, i4, i5])

o2 = Order.objects.create(food=f2, client=c1, worker=w1)
o2.ingredients.set([i2, i4])

o1_price = o1.food.start_price + sum([x.extra_price for x in o1.ingredients.all()])
o2_price = o2.food.start_price + sum([x.extra_price for x in o2.ingredients.all()])
o1_o2_full_price = o1_price + o2_price


# В ресторане большой выбор блюд и ингредиентов.
# В одном блюде могут быть несколько ингредиентов и
# один ингредиент может использоваться в нескольких блюдах
i1.orders.all()  # Определяет в каких заказах был этот ингридиент
i4.orders.all()  # Здесь выведет 2 заказа, так как он использовался в обеих



