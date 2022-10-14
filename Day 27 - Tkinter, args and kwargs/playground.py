def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    # print(total)


add(1, 2, 3, 4, 5, 6, 7, 8, 9)


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=10)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Mazda")

print(my_car.make)
