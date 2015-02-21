# CS223P - Python Programming

# Author Name: Kathy Saad
# Project Title: Assignment 2 - Vigenere Cipher
#		   Part 1 - Ciphering a Message
# Project Status: Working
# External Resources:
#	Class notes
#	https://www.python.org/
#	http://inventwithpython.com/hacking/chapter19.html
#	http://rosettacode.org/wiki/Vigen%C3%A8re_cipher#Python
#	http://web.cs.mun.ca/~michael/c/ascii-table.html

import sys

def main():
	inputfile = sys.argv[1]
	codeword = []
	codeword = sys.argv[2]
	cwIndex = 0
	count = 0
	original_msg = []
	cipherList = []
	codewordList = []
	list1 = [] # list for ascii values (btwn 0 and 25) of original message
	list2 = [] # list for ascii values (btwn 0 and 25) of codeword
	list3 = [] # final cipher list
	bitlist = []

	for letter in codeword:
		ascii_of_cw = ord(letter) - ord('a')
		list2.append(ascii_of_cw)

	inputfile.find('.')
	outputfilename = inputfile[:inputfile.find('.')] + '-cipher' + inputfile[inputfile.find('.'):]

	with open(inputfile, 'r') as ifh:
		with open(outputfilename, 'w') as ofh: # creating the output file with 'open'
			for line in ifh: # for each line in the input file
				for char in line: # for each character in the line
					if char.isalpha():
						if char.isupper():
							list1.append(ord(char) - ord('A'))
							bitlist.append('upper')
						else: # char.islower()
							list1.append(ord(char) - ord('a'))
							bitlist.append('lower')

						list3.append((int(list1[count]) + int(list2[cwIndex])) % 26)

						# Commented out the line below because it was used for testing purposes
						#print('[{} {}]'.format(char, codeword[cwIndex]), end = '')

						original_msg.append(char)
						codewordList.append(codeword[cwIndex])

						cwIndex = (cwIndex + 1) % len(codeword)
				
					else: # char == ' '
						list1.append(-88)
						list3.append(-88)
						original_msg.append(' ')
						codewordList.append(' ')
						bitlist.append(' ')

					count += 1

				i = 0
				for value in list3:
					if bitlist[i] == 'upper':
						cipherList.append(chr(value + ord('A')))
					elif bitlist[i] == 'lower':
						cipherList.append(chr(value + ord('a')))
					else:
						cipherList.append(' ')
					i += 1

				# Commented out the lines below because they were used for testing purposes
				#print('\nlist1: {}'.format(list1))
				#print('list2: {}'.format(list2))
				#print('list3: {}'.format(list3))

				#print('original message: {}'.format(original_msg))
				#print('codeword list: {}'.format(codewordList))
				#print('cipher message: {}'.format(cipherList))

				print(''.join(cipherList), file = ofh, end = '')

if __name__ == '__main__':
	main()