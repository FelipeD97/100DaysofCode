# Nested Functions

# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function()


# outer_function()

# Python Decorator Function

import time
from turtle import delay


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


@delay_decorator
def say_bye():
    print("bye")


def say_greeting():
    print("How are you?")


say_hello()
say_bye()
say_greeting()
