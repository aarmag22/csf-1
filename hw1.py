# Name: Royce Jensen
# Evergreen Login: jenroy30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

# x^2-5.86x+8.5408

a = 1
b = -5.86
c = 8.5408

# Positive
pos = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
# Negative
neg = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a

sol = str(pos)+', '+str(neg)

print(sol)

###
### Problem 2
###

print "Problem 2 solution follows:"

# Import the stuffs and screw namespace
from hw1_test import *

# Print the stuffs.
print(str(a)+'\n'+str(b)+'\n'+str(c)+'\n'+str(d)+'\n'+str(e)+'\n'+str(f))

###
### Problem 3
###

print "Problem 3 solution follows:"

print(str((a and b) or (not c) and not (d or e or f)))

###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").