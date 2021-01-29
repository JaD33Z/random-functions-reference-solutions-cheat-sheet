                   ########## SPARE-PARTS ##########

########## MY BIN OF RANDOM FUNCTIONS FOR VARIOUS THINGS ###############
######## A PYTHON PROBLEM-SOLVING SOLUTIONS REFERENCE SHEET ##################


############## RETURNING STRINGS:
def greet(name):
    return ("Hello, " + name + " how are you doing today?")


####### FIZZ-BUZZ QUESTION:
def fizz_buzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print("fizz")
        if i % 5 == 0:
            print("buzz")
        if i % 3 and i % 5 == 0:
            print("fizz-Buzz")
        else:
            print(i)


############ CONVERT NUMBER TO DOLLARS AND CENTS:

def format_money(amount):
    if amount >= 0:
        return '${:.2f}'.format(amount)


###### CREATE A PHONE NUMBER:
#Function that accepts an array of 10 integers
# (between 0 and 9), that returns a string of those numbers
# in the form of a phone number.

def create_phone_number(n):
    one = "".join(map(str, n[:3]))
    two = "".join(map(str, n[3:6]))
    three = "".join(map(str, n[6:]))
    return f"({one}) {two}-{three}"


########### MULTIPLY:

def multiply(a, b):
    multiply = a * b
    return multiply


######## CAPITALIZE A STRING:

capitalize_word = str.capitalize


###### FUNCTION TO CAPITALIZE STRING:

def capitalize_word(word):
    return word.title()


####### IS IT EVEN?:

def is_even(n):
    return n % 2 == 0


########### ABREVIATE A TWO WORD NAME:

def abbrevName(name):
    final_name = []
    name_list = name.split()
    for n in name_list:
        final_name.append(n[0].upper())
    return ".".join(final_name)


###### SUM OF SINGLE ITEMS IN ARRAY:

def repeats(arr):
    return sum([ num for num in arr if arr.count(num) == 1])



####  NUMBERING LETTERS A-Z THEN ADDING THE SUM 0F CHOSEN WORD/STRING:
# EXAMPLE: a=1, b=2, etc.

def words_to_nums(s):
    return sum(ord(letter) - 96 for letter in s)


######## QUARTER OF THE YEAR:
# Given a month as an integer from 1 to 12,
# return to which quarter of the year it belongs as an integer number.

def quarter_of(month):
    if month >= 1 and month < 4:
        return 1
    elif month >= 4 and month < 7:
        return 2
    elif month >= 7 and month < 10:
        return 3
    else:
        return 4


########   REMOVE CONSECUTIVE DUPLICATE WORDS:

import string
from itertools import groupby
def remove_consecutive_duplicates(s):
    return " ".join([x for x, y in groupby(s.split())])


##### ALTERNATE CASE:
# switch every letter in string from upper to lower
# and from lower to upper. E.g: Hello World -> hELLO wORLD

def alternateCase(s):
    return s.swapcase()


######## REPEAT STRING N TIMES:
# repeats the given string exactly "count" times.

def repeat_str(repeat, string):
    return repeat * string


######### RETURN EVEN NUMBERED CHARACTERS OF A STRING:
# function that returns a sequence (index begins with 1)
# of all the even characters from a string

def even_chars(st):
    if len(st) > 1 and len(st) < 100:
        return list(st[1::2])

    else:
        return "invalid string"


##### DETECTING IF PANGRAM OR NOT:
# A pangram is a sentence that contains every single letter
# of the alphabet at least once. For example,
# the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once.

from collections import Counter
def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    diff = word - letters
    return len(diff) == 0


########## REMOVES VOWELS FROM STRINGS, MAKES ACRONYM:

def string_task(s):
    s = s.lower()
    return ''.join('.'+ i for i in s if i not in 'aeiouy')




###################### ARRAYS AND LIST RELATED ########################

########## GET NAME BY INDEX NUMBER: DICTIONARIES, KEY, VALUE.

def get_planet_name(id):
    return {1: "Mercury",
            2: "Venus",
            3: "Earth",
            4: "Mars",
            5: "Jupiter",
            6: "Saturn",
            7: "Uranus",
            8: "Neptune",
            }.get(id)


########## DIFFERENCE BETWEEN OLDEST AND YOUNGEST IN A GROUP:

def difference_in_ages(ages):
    age = sorted(ages)
    return (age[0], age[-1], (age[-1] - age[0]))



####### SHORT STRING/LONG STRING/SHORTSTRING: SORTING, ALGORITHMS:
# EXAMPLE: ('1', '22') = '1221'

def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    elif len(a) < len(b):
        return a + b + a



######## RETURN SUM OF ALL POSITIVE NUMBERS IN A LIST:

import math
def positive_sum(arr):
    return sum(x for x in arr if x > 0)



######### VOWEL COUNT: COUNTING SPECIFIC ITEMS IN STRING/LIST:

def get_count(input_str):
    num_vowels = 0
    for i in input_str:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            num_vowels = num_vowels + 1

    return num_vowels



####### CHECK LIST/ARRAY FOR A SPECIFIC VALUE:

def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False


########## FINDING FIRST NON-CONSECUTIVE ITEM IN AN ARRAY:

def first_non_consecutive(arr):
    for i in range(1, len(arr)):

        if arr[i] - arr[i - 1] > 1:
            return arr[i]


# ############ CONSECUTIVE NUMBERS:
# You are given a list of unique integers arr, and two integers a and b.
# Check whether or not a and b appear consecutively in arr,
# and return a boolean value.

def consecutive(arr, a, b):
    x = arr.index(a)
    y = arr.index(b)
    return abs(x-y) == 1


######### ARRAY PLUS ARRAY:

def array_plus_array(arr1, arr2):
    num = sum(arr1) + sum(arr2)
    return num


########### TOTAL AMOUNT OF POINTS IN EACH GAME:
#  The result of each match look like "x:y". Results of all
#  matches are recorded in the collection.
# For example: ["3:1", "2:2", "0:1", ...]

def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))



############# FINDING THE ITEM THAT OCCURRS ODD NUMBER OF TIMES IN AN ARRAY:
# Given an array of integers, find the one that appears an odd number of times.

def find_it(seq):
    seq_size = len(seq)
    for i in range(0, seq_size):
        count = 0
        for j in range(0, seq_size):
            if seq[i] == seq[j]:
                count += 1

        if (count % 2 != 0):
            return seq[i]
    return -1