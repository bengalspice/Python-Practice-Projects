"""
Area Calculator based on shape
The program will:
1. Prompt users to select a shape to analyze;
2. Calculate the area based on the shape selected;
3. Prints the area of the shape
"""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()


print "The calculator is starting up ..."

print "Current time is %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()

if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1)
  print ("Area: %.2f \n%s" % (area, hint))
elif option == 'T':
  base = float(raw_input("Enter the base: "))
  height = float(raw_input("Enter the height: "))
  area = (base * height)/2
  print "Uni Bi Tri..."
  sleep(1)
  print ("Area: %.2f \n%s" % (area, hint))
else: 
	print "You've entered GARBAGE! Exiting..."
