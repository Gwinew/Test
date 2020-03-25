# -*- coding: utf-8 -*-

#Formating Subtitles

# We have two standard type to formating subtitles:
# The first is the old formatting used by python 2.0+
# The secound and last is new formatting used by python 3.0+
#
# In the old formatting we use sign "%" inside sentence in place where we want put the argument and outside of sentence where we need to define the argument.
# We cannot use "%" alone, we need use it with correctly type like "%s", "%f" etc.
#
# In the new formatting we use "{}" insted %. We can put "{}" alone or with type inside like "{:f}, {:s} etc.
#
# To nie może się tutaj znaleźć
#
# Raw - Old version
#
# %r is raw record. It means than in this one record we can input anything we want - digits, strings, floats.
# For example in correct records.
currency = "dolar"
us = 1
pln = 4.08244915
print("Actualy %d %s cost %.2f PLN" %(us, currency, pln))
#
# Using %r is:
print("Actualy %r %r cost %r PLN" %(us, currency, pln))
#
#
# Change the place in sentence
#
# This option is doesn't exist in old version.
# We can using the number inside formating to choose record.
print("{} have {}".format("Alice","cat"))
print("{1} have {0}".format("Alice","cat"))
#
# Elements are numbering from "0", that's why Alice is on position "0" and cat on "1".

