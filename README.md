CS223P - Python Programming

Author Name: Kathy Saad
Project Title: Assignment 3 - Classes - Cartesian 2D Coordinates
Project Status: Working
External Resources:
- https://www.python.org/
- https://www.google.com/

**********************************************************************************************************************

Instructions:

    Write a class that defines a two-dimensional Cartesian coordinate. Write the class such that the following Python program executes correctly. Save the class and the main function in a file named Cartesian2D.py.

    The two-dimensional Cartesian coordinate and main function must all be in the same file and named cartesian_demo.py.

    #/usr/bin/env python3.3
    #
    # Your header here
    #

    # Two-dimensional Cartesian coordinate
    #  class definition here
    class Cartesian2D:
      def __init__(self):
        # etc.

    def main( ):
      a = Cartesian2D(2.3, 3.4)
      b = Cartesian2D(4.5, 1.8)
      c = Cartesian2D(8.1, 0.3)
      print("The distance from a to b is {}".format(a.distanceTo(b)))
      print("The distance from b to c is {}".format(b.distanceTo(c)))
      d = a + b
      print("a + b = ({},{})".format(d.x, d.y))
      d = c - b
      print("c - b = ({}, {})".format(d.x, d.y))
      print("The length of a is {}".format(a.length()))
      print("The length of b is {}".format(b.length()))
      print("The length of c is {}".format(c.length()))
      # the normalize method returns a unit length vector
      unita = a.normalize()
      unitb = b.normalize()
      unitc = c.normalize()
      print("The length of unit a is {}".format(unita.length()))
      print("The length of unit b is {}".format(unitb.length()))
      print("The length of unit c is {}".format(unitc.length()))
      if a == b:
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
      print("dot(unita, unitb = {}".format(g))
      print("dot(d, e) = {}".format(h))


if __name__ == "__main__":
  main( )

**********************************************************************************************************************

Output:

	The distance from a to b is 2.7202941017470885
	The distance from b to c is 3.8999999999999995
	a + b = (6.8, 5.2)
	c - b = (3.5999999999999996, -1.5)
	The length of a is 4.104875150354758
	The length of b is 4.846648326421054
	The length of c is 8.105553651663778
	The length of unit a is 1.0
	The length of unit b is 1.0
	The length of unit c is 1.0
	a is not equal to b
	X: 2.2412374708168414, Y: 3.3131336525118527
	The length of d is 4.0
	dot(a, b) = 16.47
	dot(unita, unitb) = 0.827850924612497
	dot(d, e) = 13.245614793799952
