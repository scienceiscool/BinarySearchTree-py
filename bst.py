# CS223P - Python Programming
#
# Author Name: Kathy Saad
# Project Title: Assignment 4 - More Classes - Binary Search Tree
# Project Status: Working
# External Resources:
#	Class notes and handouts
#	https://www.python.org/

import random
import sys

def writeTree(tree, file_handle):
	counter = 0

	print('digraph BST{')
	file_handle.write('digraph BST{' + '\n')

	print('node [fontname = "Helvetica"];')
	file_handle.write('\t' + 'node [fontname = "Helvetica"];' + '\n')
	
	_inorder(tree._root, counter, file_handle)

	print('}')
	file_handle.write('}')

def _inorder(node, counter, file_handle):
	if node != None:
		if node.left == None:
			counter += 1
			print('\t' + 'null{} [shape=point];'.format(counter))
			file_handle.write('\t' + 'null{} [shape=point];'.format(counter))
			print('\t' + str(node.data) + ' -> ' + 'null{};'.format(counter))
			file_handle.write('\t' + str(node.data) + ' -> ' + 'null{};'.format(counter))
		else:
			print('\t' + str(node.data) + ' -> ' + str(node.left.data))
			file_handle.write('\t' + str(node.data) + ' -> ' + str(node.left.data))

		if node.right == None:
			counter += 1
			print('\t' + 'null{} [shape=point];'.format(counter))
			file_handle.write('\t' + 'null{} [shape=point];'.format(counter))
			print('\t' + str(node.data) + ' -> ' + 'null{};'.format(counter))
			file_handle.write('\t' + str(node.data) + ' -> ' + 'null{};'.format(counter))
		else:
			print('\t' + str(node.data) + ' -> ' + str(node.right.data))
			file_handle.write('\t' + str(node.data) + ' -> ' + str(node.right.data))

		counter = _inorder(node.left, counter, file_handle)
		counter = _inorder(node.right, counter, file_handle)
		return counter

	else:
		return counter

# TREE CLASS

class Tree:
	def __init__(self):
		self._root = None

	def insert(self, number):
		new_node = Node(number, None)
		self._insert(new_node)

	def _insert(self, node_to_insert):
		temp1 = self._root
		temp2 = None

		while temp1 != None:
			temp2 = temp1
			if node_to_insert.data < temp1.data:
				temp1 = temp1.left
			else:
				temp1 = temp1.right

		node_to_insert.parent = temp2

		if temp2 == None:
			self._root = node_to_insert
		elif temp2.data > node_to_insert.data:
			temp2.left = node_to_insert
		else:
			temp2.right = node_to_insert

	def _minimum(self, ptr):
		while ptr.left != None:
			ptr = ptr.left
		return ptr

	def _maximum(self, ptr):
		while ptr.right != None:
			ptr = ptr.right
		return ptr

	def search(self, key):
		temp1 = self._root

		return self._search(temp1, key)

	def _search(self, x, k):
		while x != None and k != x.data:
			if k < x.data:
				x = x.left
			else:
				x = x.right
		return x

	def remove(self, key):
		node_to_remove = self.search(key)

		if node_to_remove == None:
			return False
		else:
			self._remove(node_to_remove)
			return True

	def _remove(self, z):
		if z.left == None:
			self._transplant(z, z.right)
		elif z.right == None:
			self._transplant(z, z.left)
		else:
			y = self._minimum(z.right)
			if y.parent != z:
				self._transplant(y, y.right)
				y.right = z.right
				y.right.parent = y
			self._transplant(z, y)
			y.left = z.left
			y.left.parent = y

	def _transplant(self, u, v):
		if u.parent == None:
			self._root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		if v != None:
			v.parent = u.parent

# NODE CLASS

class Node:
	__slots__ = {'_data', '_parent', '_left', '_right'}

	def __repr__(self):
		if self._parent == None:
			p = 'none'
		else:
			p = str(self._parent._data)
		if self._left == None:
			l = 'none'
		else:
			l = str(self._left._data)
		if self._right == None:
			r = 'none'
		else:
			r = str(self._right._data)
		return 'parent: {} left: {} right: {} data: {}'.format(p, l, r, self._data)

	def __init__(self, data, parent):
		self._data = data
		self._parent = parent
		self._left = None
		self._right = None

	#def __str__(self):
	#	return '{} -> {}\n{} -> {}'.format(self.data, self.right.data, self.data, self.left.data)

	def getData(self):
		return self._data

	def setData(self, new_data):
		self._data = new_data

	def getParent(self):
		return self._parent

	def setParent(self, new_parent):
		self._parent = new_parent

	def getLeft(self):
		return self._left

	def setLeft(self, new_left):
		self._left = new_left

	def getRight(self):
		return self._right

	def setRight(self, new_right):
		self._right = new_right

	data = property(getData, setData)
	parent = property(getParent, setParent)
	left = property(getLeft, setLeft)
	right = property(getRight, setRight)

# MAIN FUNCTION

def main():
	if len(sys.argv) < 2:
		print('Please provide the number of keys to enter')
		sys.exit(1)
	s = int(sys.argv[1])
	parts = int(s / 3)
	t = Tree()
	r = list(range(1, s+1))

	print('Randomly inserting the numbers from 1 to {}'.format(len(r)))

	random.shuffle(r)

	for i in r:
		print('Inserted {}'.format(i))
		t.insert(i)
	f = open('a.dot', 'w')
	writeTree(t, f)
	f.flush()
	f.close()
	random.shuffle(r)

	for n in range(1, 3):
		m = r[(n - 1) * parts : (n * parts)]
		print(len(m))
		for i in m:
			print('Removed {}'.format(i))
			v = t.remove(i)
			if v:
				print('\tCompleted')
			else:
				print('\tError')
		c = chr(n + 97)
		filename = str(c) + '.dot'
		f = open(filename, 'w')
		writeTree(t, f)
		f.flush()
		f.close()

# CALL TO MAIN FUNCTION

if __name__ == "__main__":
	main()
