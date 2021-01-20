"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util

import random

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")
  name = input("What is your first name? ")
  lastname = input("What is your last name? ")
  print("Hello, "+name+" "+lastname+"! I'm glad I have met you.")
  feeling = input("Okay, "+name+", how is your day so far? ")
  if (feeling == "good"):
    print("I'm glad your day has been good. It makes me feel happy.")
    good_day = input("What made your day good? ")
    print("That's good to hear.")
  if (feeling == "bad"):
    print("Oh my! That's no good!")
    bad_day = input("What made your day bad? ")
    print("Well I hope that everything gets better soon.")
  color = input("So tell me, "+name+", what is your favorite color? ")
  if (color == "green"):
    print("That's my favorite color too!")
  else:
    print("That's cool.")
  nickname = input("I'm curious, "+name+". Do you have a nickname? ")
  if (nickname == "yes"):
    what_nickname = input("What is it? ")
    print("Wow. I like that nickname.")
  season = input("What is your favorite season, "+name+"? ")
  if(season == "winter"):
    print("I love how the trees look when it snows. Winter is definitely a pretty season.")
  elif(season == "fall"):
    print("I love fall! The way the leaves look when they change is my favorite part.")
  elif(season == "spring"):
    print("Spring is a lovely season. My favorite part is the rain.")
  elif(season == "summer"):
    print("I should have guessed. Summer is a very relaxing season and it is pretty warm too.")
  food = input("Say, "+name+". What is your favorite food? ")
  if(food == "")



if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()