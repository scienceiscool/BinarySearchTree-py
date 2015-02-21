CS223P - Python Programming

Author Name: Kathy Saad<br>
Project Title: Assignment 4 - More Classes - Binary Search Tree<br>
Project Status: Working<br>
External Resources:<br>
- Class notes and handouts<br>
- https://www.python.org/

*******************************************************************************************************************************************

Sample run:

	kat@ubuntu:~/Desktop/MyVMSharedFolder$ python3.4 bst.py 10
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

Commands to create PDFs:

		dot -Tpdf -o a20.pdf a.dot
		dot -Tpdf -o b20.pdf b.dot
		dot -Tpdf -o c20.pdf c.dot