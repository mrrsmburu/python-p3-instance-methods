#!/usr/bin/env python3

class Person:
    # Class body goes here

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

    def talk(self):
        print("Hello World!")

    #Instance method definition
        person = Person("John")
        person.greet()  # Output: Hello, my name is John
        person.talk()
