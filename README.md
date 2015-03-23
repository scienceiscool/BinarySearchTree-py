#CPSC 223P - Python Programming

__Author Name:__ Kathy Saad<br>
__Project Title:__ Assignment 4 - More Classes - Binary Search Tree<br>
__Project Status:__ Working<br>
__External Resources:__<br>
- Class notes and handouts<br>
- https://www.python.org/

*******************************************************************************************************************************************

__Instructions:__ In all the classes for this assignment, use of the following Python language features is mandatory:

- Properties
- Slots
- Name implementation details (e.g. private data members) accordingly

It is strongly recommended the students read and understand <http://docs.python.org/py3k/reference/datamodel.html> and <http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html>.
 
 
1. Write one or more classes that define a binary tree which can be used with the following main function.

```
import random
import sys

def main( ):
 if len(sys.argv) < 2:
  print('Please provide the number of keys to enter.')
  sys.exit(1)
 s = int(sys.argv[1])
 parts = int(s/3)
 t = Tree( )
 r = list(range(1,s+1))

 print('Randomly inserting the numbers from 1 to {}.'.format(len(r)))

 random.shuffle(r)

 for i in r:
  print('inserted {}'.format(i))
  t.insert(i)
 f = open('a.dot', 'w')
 writeTree(t, f)
 f.flush( )
 f.close( )
 random.shuffle(r)

 for n in range(1, 3):
  m = r[(n-1) * parts : (n * parts)]
  print(len(m))
  for i in m:
   print('removed {}'.format(i))
   v = t.remove(i)
   if v:
    print('\tcompleted.')
   else:
    print('\terror.')
  c = chr(n + 97)
  filename = str(c) + '.dot'
  f = open(filename, 'w')
  writeTree(t, f)
  f.flush( )
  f.close( )
```

The output of the program is a file in DOT syntax. The output of your program must be passed to the program 'dot', part of Graph Viz, to create an visualization of your tree. An example output file is the following: 

digraph BST{<br>
&nbsp;&nbsp;node [fontname="Helvetica"];<br>
&nbsp;&nbsp;7 -> 2;<br>
&nbsp;&nbsp;2 -> 1;<br>
&nbsp;&nbsp;null1 [shape=point];<br>
&nbsp;&nbsp;1 -> null1;<br>
&nbsp;&nbsp;null2 [shape=point];<br>
&nbsp;&nbsp;1 -> null2;<br>
&nbsp;&nbsp;null3 [shape=point];<br>
&nbsp;&nbsp;2 -> null3;<br>
&nbsp;&nbsp;7 -> 9;<br>
&nbsp;&nbsp;null4 [shape=point];<br>
&nbsp;&nbsp;9 -> null4;<br>
&nbsp;&nbsp;null5 [shape=point];<br>
&nbsp;&nbsp;9 -> null5;<br>
}

An example command is:<br>
$dot -Tpdf -o output.pdf input.dot

*******************************************************************************************************************************************

__Sample run:__

	$python3.4 bst.py 10
	Randomly inserting the numbers from 1 to 10
	Inserted 2
	Inserted 10
	Inserted 1
	Inserted 3
	Inserted 5
	Inserted 7
	Inserted 9
	Inserted 6
	Inserted 4
	Inserted 8
	digraph BST{
	node [fontname = "Helvetica"];
		2 -> 1
		2 -> 10
		null1 [shape=point];
		1 -> null1;
		null2 [shape=point];
		1 -> null2;
		10 -> 3
		null3 [shape=point];
		10 -> null3;
		null4 [shape=point];
		3 -> null4;
		3 -> 5
		5 -> 4
		5 -> 7
		null5 [shape=point];
		4 -> null5;
		null6 [shape=point];
		4 -> null6;
		7 -> 6
		7 -> 9
		null7 [shape=point];
		6 -> null7;
		null8 [shape=point];
		6 -> null8;
		9 -> 8
		null9 [shape=point];
		9 -> null9;
		null10 [shape=point];
		8 -> null10;
		null11 [shape=point];
		8 -> null11;
	}
	3
	Removed 5
		Completed
	Removed 10
		Completed
	Removed 3
		Completed
	digraph BST{
	node [fontname = "Helvetica"];
		2 -> 1
		2 -> 6
		null1 [shape=point];
		1 -> null1;
		null2 [shape=point];
		1 -> null2;
		6 -> 4
		6 -> 7
		null3 [shape=point];
		4 -> null3;
		null4 [shape=point];
		4 -> null4;
		null5 [shape=point];
		7 -> null5;
		7 -> 9
		9 -> 8
		null6 [shape=point];
		9 -> null6;
		null7 [shape=point];
		8 -> null7;
		null8 [shape=point];
		8 -> null8;
	}
	3
	Removed 7
		Completed
	Removed 8
		Completed
	Removed 1
		Completed
	digraph BST{
	node [fontname = "Helvetica"];
		null1 [shape=point];
		2 -> null1;
		2 -> 6
		6 -> 4
		6 -> 9
		null2 [shape=point];
		4 -> null2;
		null3 [shape=point];
		4 -> null3;
		null4 [shape=point];
		9 -> null4;
		null5 [shape=point];
		9 -> null5;
	}

*******************************************************************************************************************************************

__To create visual PDFs of the tree with GraphViz:__

		$dot -Tpdf -o a20.pdf a.dot
		$dot -Tpdf -o b20.pdf b.dot
		$dot -Tpdf -o c20.pdf c.dot
