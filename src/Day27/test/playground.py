# def add(*args): --> args here is a tuple
#     result = 0
#     for n in args:
#         result += n
#     return result

# print(add(1, 2, 3, 4, 5, 6, 7))

# def calculate(**kwargs): --> kwargs here is a dictionary
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"Key: {key}")
    #     print(f"Value: {value}")
    # print(kwargs["add"])
    # print(kwargs["multiply"])

# calculate(add=5, multiply=6)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)