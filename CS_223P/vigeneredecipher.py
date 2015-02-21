# CS223P - Python Programming
#
# Author
#	Name: Kathy Saad
# Project
#	Title: Assignment 2: Vigenere Cipher
#		   Part 2 - Deciphering a Message
#	Status: Working
# External Resources
#	Class notes
#	python.org
#	http://inventwithpython.com/hacking/chapter19.html
#	http://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python
#	http://web.cs.mun.ca/~michael/c/ascii-table.html

import sys

def main():
	inputfile = sys.argv[1]
	codeword = sys.argv[2]
	list1 = []
	#list2 = []
	#clearList = []
	#count = 0
	#cwIndex = 0

	#for letter in codeword:
	#	list2.append(ord(letter) - ord('a'))

	inputfile.find('.')
	outputfilename = inputfile[:inputfile.find('.')] + '-clear' + inputfile[inputfile.find('.'):]

	with open(inputfile, 'r') as ifh:
		with open(outputfilename, 'w') as ofh:
			for line in ifh:
				for char in line:
					if char.isalpha():
						if char.isupper():
							list1.append(chr((ord(char) - ord('A')) + 65))
						else: # char.islower()
							list1.append(chr((ord(char) - ord('a')) + 97))

						#clearChar = ((int(list1[count]) - int(list2[cwIndex])) % 26)
						#clearList.append(chr(clearChar))
						#cwIndex = (cwIndex + 1) % len(codeword)

					else: # char == ' '
						#clearList.append(' ')
						list1.append(' ')

					#count += 1

				# Commented out the lines below because they were used for testing purposes
				#print('\nlist1: {}'.format(list1))

				#print('list2: {}'.format(list2))
				#print('clear list: {}'.format(clearList))
				#print(''.join(clearList), file = ofh, end = '')

				print(''.join(list1), file = ofh, end = '')

if __name__ == '__main__':
	main()