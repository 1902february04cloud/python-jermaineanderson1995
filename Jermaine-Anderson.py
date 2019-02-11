#!/usr/bin/env python3

'''
General Instructions are in the README.md file

Use the main function for testing purposes and to show me results for all functions.
'''

#Modules
import math
import logging
import logging.config
import os

def main():
	print('\n')
	print(reverse('Jermaine')+'\n')
	print(acronym('Portable Network Graphics')+'\n')
	print(whichTriangle(10, 10, 15)+'\n')
	print(scrabble('cabbage'))
	print()
	print(armstrong(153))
	print()
	print(primeFactors(100))	
	print()
	print(pangram('The quick brown fox jumps over the lazy dog.'))
	print()
	print(sort([2,4,5,9,3,6,12,1,3,1]))
	print()
	print(rotate(13,'The quick brown fox jumps over the lazy dog')+'\n')
	evenAndOdds()

'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	print('1. Reverse a String. Example: Jermaine')
	#Local Variables
	string_length = 0
	count = 1
	string_reversed = ''

	#Get Length of String 
	for char in string:
		string_length += 1

	for char in string:
		#Add Last Character to a String
		string_reversed += string[string_length - count]
		count += 1
	str = string_reversed
	return str
'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
	print('2. Convert a phrase to its acronym. Example: Portable Network Graphics')
	#Split the phrase into a list
	phrase_split = phrase.split(' ')
	
	#Variables
	count = 0
	str = '('
	
	#Go through a list
	while count < len(phrase_split):
		#Grab each word from list
		word = phrase_split[count]
		#If the first character in a word uppercase, save it
		if word[0] != word[0].lower():
			str += word[0]
		count += 1
	str += ')'
	return str
'''	
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	print('3. Determine a Triangle. Example: SideA:10  SideB:10  SideC:15')		
	if sideOne == sideTwo == sideThree:
		str = 'This is an equilateral triangle'
	elif sideOne == sideTwo or sideOne == sideThree or sideTwo == sideThree:
		str = 'This is an isosceles triangle'
	else:	
		str = 'This is an scalene triangle'
	return str
'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
	print('4. Compute the Scrabble Score. Example: Cabbage')
	#Variables
	str = 0
	letter_scores = {'a':1,'e':1,'i':1,'o':1,'u':1,'l':1,'n':1,'r':1,'s':1,'t':1,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,'y':4,'k':5,'j':8,'x':8,'q':8,'z':10}

	#Get each character	
	for char in word:
		char = char.lower()
		#Get score for character
		str += letter_scores[char]		
	return str
'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
	print('5. Is 154 an Armstrong?')
	#Variables
	number = str(number)
	power = len(number)
	total = 0
	
	#Get each single number from bigger number
	for num in number:
		#Turn number back into an integer
		num = math.pow(int(num),power)
		total += num
	total = int(total)
	number = int(number)
	if total == number:
		bool =  True
	else:
		bool = False	
	return bool

'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number):	
	print('6. Compute the prime factors. Example: 100')
	#Variables
	primes = []
	list = []
	finalcount = 0
	#Algorithm
	#Find factors of the number
	for count in range(1,number + 1,1):
		if (number / count).is_integer():
			primes.append(int(number / count))		
	#Get rid of duplicates
	primes = set(primes)
	
	#Sort data
	for index in primes:
		list.append(index)
	list.sort()
	return list	
'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.

The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence):
	print('7. Determine if a sentence is a pangram. \nExample: The quick brown fox jumps over the lazy dog')
	#Variables
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	sentence = sentence.lower()	
	bool = True
	#Get each character from then sentence
	for char in sentence:
		#Get each character from the alphabet
		for char in alphabet:
			'''
			Return false if the sentence does not contain 
			all of the characters from the alphabet
			'''
			if sentence.find(char) < 0:
				bool = False
	return bool
'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers):
	print('8. Sort list of integers. Example: [2,4,5,9,3,6,12,1,3,1]')
	#Variables
	case = False
	length = 0
	for number in numbers:
		length += 1
	#Loop till all numbers are in order
	while case == False:
		case = True
		#Go through the list
		for index in range(1,length,1):
			'''
			If the number in front is bigger then the 
			number behind it then swap numbers
			'''
			if numbers[index - 1] > numbers[index]:
				case = False
				tmp = numbers[index - 1]
				numbers[index - 1] = numbers[index]
				numbers[index] = tmp
	return numbers				
'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key, string):
	print('9. Create an implementation of the Caesar cipher. \nExample: ROT13 The quick brown fox jumps over the lazy dog')
	#Variables
	alphabet_char = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
	alphabet_value = {'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5 ,'f':6 ,'g':7 ,'h':8 ,'i':9 ,'j':10 ,'k':11 ,'l':12 ,'m':13 ,'n':14 ,'o':15 ,'p':16 ,'q':17 ,'r':18 ,'s':19 ,'t':20 ,'u':21 ,'v':22 ,'w':23 ,'x':24 ,'y':25 ,'z':26}
	str = ''
	
	#Get each char from string
	for char in string:
		char = char.lower()	
		#If you run into a space, save it and go to next char
		if char == ' ':
			str += ' '
			continue
		new_char_value = alphabet_value[char] + key
		#Once you reach the each of the dictionary, go back to index 0
		while new_char_value > 26:
			new_char_value = new_char_value - 26
		str += alphabet_char[new_char_value]
	return str
'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
	'''
	If the files doesn't exist then create
	If the files exist clear the data 
	'''
	with open('even.txt','w') as doc:
		doc.write('***Even Numbers***\n')
	with open('odd.txt','w') as doc:
		doc.write('***Odd Numbers***\n')
	#Variable
	list = []
	count = 0

	print('10. Save even numbers is even.txt and odd numbers in odd.txt')	
	#Get user inputs
	while count == 0:
		list.append(input('First Number:\t'))
		list.append(input('Second Number:\t'))
		list.append(input('Third Number:\t'))
		list.append(input('Fourth Number:\t'))
		list.append(input('Fifth number:\t'))
		list.append(input('Sixth Number:\t'))
		list.append(input('Seventh Number:\t'))
		list.append(input('Eighth Number:\t'))
		list.append(input('Ninth Number:\t'))
		list.append(input('Tenth Number:\t'))
		#Check if inputs are numeric
		for number in list:
			if number.isnumeric():
				count += 1
		#If an input isn't numeric, raise error and reset variables
		if count != 10:
			print('***ERROR***\nPlease Enter Only Numbers! Try again')	
			count = 0
			list = []
	
	#Grab each number user input
	for number in list:
		number = int(number)
		#Write even numbers to a file
		if number % 2 == 0:
			with open('even.txt','a+') as doc:
				number = str(number)
				doc.write(number + '\n')
		#Write odd numbers to a file
		else:
			with open('odd.txt','a+') as doc:
				number = str(number)
				doc.write(number + '\n')

if __name__ == "__main__":
    main()
