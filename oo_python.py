#!/bin/bash

import boto3
import json
from bson import json_util
import os
import sys
import csv
import datetime
import io
import re
import requests
import base64
import logging
import itertools, sys
import dateutil.parser
from pprint import pprint
import datetime
from json import JSONEncoder



##########################-------- DEFINITIONS -----------###########################
DECORATOR - a function which modifies functions
######################################################################################



# Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores. 

class Dog:
    species="canis familiaris" # class attribute - 'species'
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    # Get info just by printing the dog object    
    def __str__(self):
       return f"Use this when you want to display info about a dog by printing the dog object:  {self.name} is {self.age} years old"
     
     # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

################################### CHILD CLASSES ####################################
# Remember, to create a child class, you create new class with its own name and then 
# put the name of the parent class in parentheses.
# Add the following to the dog.py file to create three new child classes of the Dog class:
######################################################################################

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


class GenericClass:
    'This is just documentation that goes into the class'

callie = Dog("Callie","1","cairn terrier")
kona = Dog("Kona","1","rottweiler")

print(kona.name)
print(kona.age)
print(kona.species)

print("description " + kona.description())
print("what does the dog say? " + kona.speak("yaaaoooowwwwlll!"))
print(kona)


miles = JackRussellTerrier("Miles", 4, "Jack Russell Terrier")
buddy = Dachshund("Buddy", 9, "Dachshund")
jack = Bulldog("Jack", 3, "Bulldog")
jim = Bulldog("Jim", 5, "Bulldog")

######################## WHICH CLASS DOES AN OBJECT BELONG TO ########################

print(type(miles))
print(type(buddy))
print(type(jack))
print(type(jim))

######################################################################################


################### DOES AN OBJECT BELONG TO A PARTICULAR CLASS  ####################

print(isinstance(miles, Bulldog))
print(isinstance(jack, Dachshund))

######################################################################################
