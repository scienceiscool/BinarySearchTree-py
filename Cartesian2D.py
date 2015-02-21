#/usr/bin/env python3.4

# CS223P - Python Programming
#
# Author Name: Kathy Saad
# Project Title: Assignment 3 - Classes - Cartesian 2D Coordinates
# Project Status: Working
# External Resources:
#	https://www.python.org/
#	https://www.google.com/

from math import *

def dot(self, otherPoint): # postcondition: returns the dot product of two vectors
	return ((self.x * otherPoint.x) + (self.y * otherPoint.y))

class Cartesian2D: # each instance of the class will be a point consisting of two coordinates

	def __init__(self, x, y): # parameters: x - first coordinate; y - second coordinate
		self.x = x
		self.y = y

	def __add__(self, otherPoint): # purpose: adds two vectors; postcondition: returns the resulting vector
		x = self.x + otherPoint.x
		y = self.y + otherPoint.y
		return Cartesian2D(x, y)

	def __sub__(self, otherPoint): # purpose: subtracts two vectors; postcondition: returns the resulting vector
		x = self.x - otherPoint.x
		y = self.y - otherPoint.y
		return Cartesian2D(x, y)

	def __mul__(self, some_scalar): # purpose: multiplies a vector and a scalar value; postcondition: returns the resulting vector
		x = self.x * some_scalar
		y = self.y * some_scalar
		return Cartesian2D(x, y)

	def length(self): # postcondition: returns the length/magnitude of a vector
		return sqrt((self.x ** 2) + (self.y ** 2))

	def distanceTo(self, otherPoint): # postcondition: returns the distance from one vector to another
		return (self - otherPoint).length()

	def __str__(self): # postcondition: returns a string
		return 'X: {self.x}, Y: {self.y}'.format(self = self)

	def normalize(self): # postcondition: returns a unit length vector
		x = self.x / self.length()
		y = self.y / self.length()
		return Cartesian2D(x, y)

def main():

	a = Cartesian2D(2.3, 3.4)

	b = Cartesian2D(4.5, 1.8)

	c = Cartesian2D(8.1, 0.3)

	print("The distance from a to b is {}".format(a.distanceTo(b)))

	print("The distance from b to c is {}".format(b.distanceTo(c)))

	d = a + b

	print("a + b = ({}, {})".format(d.x, d.y))

	d = c - b

	print("c - b = ({}, {})".format(d.x, d.y))

	print("The length of a is {}".format(a.length()))

	print("The length of b is {}".format(b.length()))

	print("The length of c is {}".format(c.length()))

	unita = a.normalize()

	unitb = b.normalize()

	unitc = c.normalize()

	print("The length of unit a is {}".format(unita.length()))
	
	print("The length of unit b is {}".format(unitb.length()))
	
	print("The length of unit c is {}".format(unitc.length()))
	
	if (a.x == b.x) and (a.y == b.y):

		print('Somehow a is equal to b?')

	else:

		print('a is not equal to b')

	s = 4

	d = unita * s

	print(d)

	print("The length of d is {}".format(d.length()))

	e = unitb * s

	f = dot(a, b)

	g = dot(unita, unitb)

	h = dot(d, e)

	print("dot(a, b) = {}".format(f))
	
	print("dot(unita, unitb) = {}".format(g))
	
	print("dot(d, e) = {}".format(h))

if __name__ == "__main__":
	main()
