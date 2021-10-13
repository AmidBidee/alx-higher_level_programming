#!/usr/bin/python3
"""
student module

Student(first_name, last_name): Student object class
[class].to_json(): returns dictionary represention of student instance
"""


class Student:
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        _dict = {}
        if attrs:
            for attr in attrs:
                if attr in self.__dict__:
                    _dict[attr] = self.__dict__[attr]
            return _dict
        return self.__dict__
