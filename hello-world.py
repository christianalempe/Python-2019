'''
###########################################

Everything in here is a comment

DATA TYPES

# Strings
# Numbers
# Lists
# Tuples (a list you can't change -- why? -- tuples are a bit faster?!)
# Dictionaries
# Bolean

###########################################
'''

import os
os.system('clear')

# string
firstname = 'Christiana'

# number
age = 22

# list and tuple
names = ["John", "Bob", "Mary"]
names_tuple = ("John", "Bob", "Mary")

# dictionary
fav_pizza = {
    "John": "Pepperoni",
    "Bob": "Mushroom",
    "Mary": "Cheese"
}

# boolean
name = True

# some print tries
greetings = "hello my name is Christiana Lempesi"
print(greetings.split(" ")[4:6])

# names.append("Wes")
print(names)

########################### Conditional Statements

num = 5

if (num >10):
    print("Ypur number is greater than 10!")
elif(num==10):
    print("Your number is equal to 10!")
else:
    print("Your number is smaller than 10!")

########################### While and For Loops

counter = 0

while (counter < 3):
    print("The count is: ", + counter)
    counter += 1


for key, value in fav_pizza.items():
    print(key + " likes " + value + " pizza!")

# "{:,}".format(variable)

################################# FUNCTIONS

def mathit(num1, num2):
    return(num1 + num2)

outcome = 100*mathit(1, 2)

######################################################## MODULES ##########################################
'''
# basic Data Science
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data and text proccessing Natural Language Toolkit
import nltk

# basic Machine Learning 
import tensorflow as tf
from tensorflow import keras # higher level API for tensorflow
import sklearn

# create your own MODULE (think od it as a CLASS)
'''

import namer
namer.nameit("Christiana")

############################################## SQLite Database ################################

import sqlite3
from sqlite3 import Error

# create database
def sql_connection():
    try:
        con = sqlite3.connect('customer.db')
        return con
    except Error:
        print(Error)

# create table
def sql_table(con):
    # create a cursor
    # think of cursor as a messenger - we send it off to our database to do stuff
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE customer(first_name text, last_name text, email text)")
    
    # commit the change to the database
    con.commit()

# con = sql_connection()
# sql_table(con)

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO customer VALUES(?, ?, ?)', entities)   
    con.commit()

con = sqlite3.connect('customer.db')
# entities = ('Christiana', 'Lempesi', 'christianna.lempesi99@outlook.com')
# sql_insert(con, entities)

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM customer')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

sql_fetch(con)
# [print(row) for row in cursorObj.fetchall()]

con.close()