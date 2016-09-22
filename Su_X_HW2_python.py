# -*- coding: utf-8 -*-
"""
Created on Thu Sep  18 19:37:01 2016

@author: sxq
"""

#Group C&D

print (1)

"""
Write a version of a palindrome recogniser that accepts a file
name from the user, reads each line, and prints the line to the
screen if it is a palindrome.
For	Reference: Define a function is_palindrome()that recognizes 
palindromes(i.e. words that look the same written backwards). For example,
is_palindrome("radar")should return True.

"""
import string
# We could enter the file name by inputting file's name 
file_name = input('Enter the file name (ex. palindromes.txt)> ')
# since we only want to look at words, not spaces and puctuations,
# we store the spaces and punctuations of the content of the file 
# under "unwanted"
unwanted = string.punctuation + ' '

f = file_name 

# we define a function is_palindrome() that could recognize
# palindromes. 
def is_palindrome(str):
  # we remove the unwanted items of the file
  newstr = [x for x in str.lower() if x not in unwanted]
  # we use the if statement to check if the words that look the same
  # written backwards
  if newstr == newstr[::-1]:
      # if we find out the palindrome, we print the words, 
      # and return true
      print(newstr)
      return True

# we store the content in file_name into f
with open(file_name, 'r') as f:
  # we read the line in f
  for line in f:
    # we use rstrip to remove the newline (\n) at the end of the line
    if is_palindrome(line.rstrip()):
      print(line.rstrip())

# check if our function works well
is_palindrome("hannah")
is_palindrome("radar")
is_palindrome("hello")


print (2)

"""
According to Wikipedia, a semordnilap is a word or phrase that
spells a different word or phrase backwards. ("Semordnilap" is
itself "palindromes" spelled backwards.) Write a semordnilap
recogniser that accepts a file name (pointing to a list of words)
from the user and finds and prints all pairs of words that are
semordnilaps to the screen. For example, if "stressed" and
"desserts" is part of the word list, the output should include
the pair "stressed desserts". Note, by the way, that each pair by
itself forms a palindrome! 

"""
import string
# We could enter the file name by inputting file's name 

file_name = input('Enter file name (ex. semordnilaps.txt)> ')
# since we only want to look at words, not spaces and puctuations,
# we store the spaces and punctuations of the content of the file 
# under "unwanted"
unwanted = string.punctuation + ' '
#we define a function finding() to store strings in the file
def finding(str):
  finding_str = [x for x in str.rstrip().lower() if x not in unwanted]
  return finding_str

found = []
# we open the file
with open(file_name, 'r') as f:
  # we read each lines of the file
  for line in f:
    # use if statements to check if any semordnilaps pairs exist
    # if the pairs exist, print the pair
    if finding(line)[::-1] in found:
      print(finding(line), finding(line)[::-1])
    else:
      found.append(finding(line))
      
print (3)
"""
Write a procedure char_freq_table()that, when run in a terminal,
accepts a file name from the user, builds a frequency listing of
the characters contained in the file, and prints a sorted and
nicely formatted character frequency table to the screen. 
"""
# we define a function char_freq_table() that prints a sorted and 
# nicely formatted character frequency table to the screen,

def char_freq_table(file_name):
  # we define freq
  freq = {}
  # we open the file 
  with open(file_name, 'r') as f:
    # Since spaces and newlines are items that we do not want to
    # take into account, we need to remove those items of the file
    # let str store the characters in the file
    str = [x for x in f.read() if x not in [' ','\n']]
    # we compute the frequency of each character    
    for i in str:
      if i in freq:
        freq[i] += 1
      else:
        freq[i] = 1

    # we display a sorted and nicely formatted character frequency
    # table to the screen 
    print('Characters Frequency Table:')
    for char in sorted(list(freq.items()), key=lambda x: x[1], reverse=True):
      print(char[0], freq[char[0]])

# check 
file_name = input('Enter file name (ex. poem.txt)> ')
char_freq_table(file_name)

print (4)

"""
The International Civil Aviation Organization (ICAO) alphabet
assigns code words to the letters of the English alphabet
acrophonically (Alfa for A, Bravo for B, etc.) so that critical
combinations of letters (and numbers) can be pronounced and
understood by those who transmit and receive voice messages by
radio or telephone regardless of their native language, especially
when the safety of navigation or persons is essential. Here is a
Python dictionary covering one version of the ICAO alphabet: d =
{'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
'y':'yankee', 'z':'zulu'} Your task in this exercise is to write a 
procedure speak_ICAO()able to translate any text (i.e. any string)
into spoken ICAO words. You need to import at least two libraries:
osand time. On a mac, you have access to the system TTS
(Text-To-Speech) as follows:os.system('say'+msg), wheremsgis the
string to be spoken. (Under UNIX/Linux and Windows, something
similar might exist.) Apart from the text to be spoken, your
procedure also needs to accept two additional parameters: a float
indicating the length of the pause between each spoken ICAO
word, and a float indicating the length of the pause between each
word spoken. 
"""

import time, os
from string import punctuation
# we creat the icao dictionary
dict = { 'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
         'f':'foxtrot','g':'golf', 'h':'hotel', 'i': 'india', 'j':'juliett', 
         'k':'kilo', 'l':'lima', 'm':'mike', 'n': 'november', 'o':'oscar', 
         'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
         'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray',
         'y':'yankee', 'z':'zulu'}
# we define a function speak_ICAO. The default length of pause are 1s and 3s each.
def speak_ICAO(name, icao_pause=1, word_pause=3):  
    # we open the file.  
    file = open(name)
    # convert uppercase to lowercase.
    word = file.read().lower()
    # remove punctuations in the file and replace them with space
    for pun in ('!','?',',','.',"'",'"',':'):
        word = word.replace(pun,'')
    # replace '\n' with space
    word = word.replace('\n',' ')
    # we split every words
    word = word.split(' ')
    # Use for loops to translate every alphabet to icao words and speak.
    for i in range(len(word)):
        # Make a pause between each words.
        time.sleep(word_pause)
        for j in range(len(word[i])):
            for alph, icao in dict.items():
                # translate every alphabet in the word to icao words and to speak.
                if word[i][j] == alph:
                    os.system('say '+icao)
                    # Make a pause between each icao words.
                    time.sleep(icao_pause)
# check
speak_ICAO(input('Enter file name') )    
#print(speak_ICAO(filename))
print (5)

"""
A hapax legomenon (often abbreviated to hapax) is a word which
occurs only once in either the written record of a language, the
works of an author, or in a single text. Define a function that given
the file name of a text will return all its hapaxes. Make sure your
program ignores capitalization. 
"""
# define a new function.
def hapax(name):
    # Open the file.  
    file = open(name)
    # convert uppercase to lowercase.(ignore capitalization)
    word = file.read().lower()
    # ignore punctuations in the file,
    # and replace them with space
    for pun in ('!','?',',','.',"'",'"',':'):
        word = word.replace(pun,'')
    # ignore '\n' and replace with space
    word = word.replace('\n',' ')
    # we split every words
    word = word.split(' ')
    # Use for loop to count the time of each word appears.
    for i in range(len(word)):
        # if the word appears only once, 
        # then we print it to the screen.
        if word.count(word[i]) == 1:
            print(word[i])

# check
print(hapax('hapax.txt'))

print (6)

"""
Write a program that given a text file will create a new text file in
which all the lines from the original file are numbered from 1 to n
(where n is the number of lines in the file). 
"""
import re
# define a new function
def numbered_line(name):
    # open the file
    file = open(name)
    # read the file and split each line
    lines = file.read().split('\n')
    for i in range(len(lines)):
        # put numbers in front of each line
        lines.insert(3*i,str(i+1))
        # insert \n after each line
        lines.insert(3*i+2,'\n')
    # we create a new file to store   
    new_file = open('new_file.txt','w')
    # write the new list lines in the file
    for i in range(len(lines)):
        new_file.writelines(lines[i])
    # close the file
    new_file.close()


# check
numbered_line('poem.txt')

print (7)

"""
Write a program that will calculate the average word length of a text
stored in a file (i.e the sum of all the lengths of the word tokens in
the text, divided by the number of word tokens). 

"""
from string import punctuation

# define a new function
def aver(name):
    # open the file.  
    file = open(name)
    # convert uppercase to lowercase.
    word = file.read().lower()
    # replace punctuations in the file with space.
    for pun in ('!','?',',','.',"'",'"',':'):
        word = word.replace(pun,'')
    word = word.replace('\n',' ')
    # we split every words
    word = word.split(' ')
    # we define a variable to store the length of total words
    sum_words = 0
    # Use for loop to add length of each word.
    for i in range(len(word)):
        sum_words += len(word[i])
    # display the average length of word
    print(sum_words/len(word))
    
# check
aver('hapax.txt')



print (8)

"""
Write a program able to play the "Guess the number"-game, where
the number to be guessed is randomly chosen between 1 and 20.
(Source: http://inventwithpython.com) This is how it should work
when run in a terminal: >>> import guess_numberHello! What is
your name?TorbjörnWell, Torbjörn, I am thinking of a number
between 1 and 20. Take a guess. 10Your guess is too low.Take
a guess.15Your guess is too low.Take a guess.18Good job,
Torbjörn! You guessed my number in 3 guesses!

"""
from random import randrange
# we define a function gtn()
def gtn():
	print("Hello! What is your name?")
	gamer_name = input()

	print('Well, %s, I am thinking of a number between 1 and 20.' % gamer_name)
	# choose a number between 1 to 20
	mynumber = randrange(1,21) 
    # create a variable tries to store the times of tries.
	tries = 0 

	while True:
		print('Take a guess.')

		gamer_guess = int(input()) 
		tries += 1

		if gamer_guess == mynumber:
			print('Good job, %s! You guessed my number in %d guesses!' % (gamer_name, tries))
			break
		elif gamer_guess < mynumber:
			print('Your guess is too low.')
		else:
			print('Your guess is too high.')

# check
gtn()

print(10)

"""
In a game of Lingo, there is a hidden word, five characters long.
The object of the game is to find this word by guessing, and in
return receive two kinds of clues: 1) the characters that are fully
correct, with respect to identity as well as to position, and 2) the
characters that are indeed present in the word, but which are
placed in the wrong position. Write a program with which one can
play Lingo. Use square brackets to mark characters correct in the
sense of 1), and ordinary parentheses to mark characters correct in
the sense of 2). Assuming, for example, that the program conceals
the word "tiger", you should be able to interact with it in the
following way: >>> import lingo snakeClue: snak(e) fiest
Clue: f[i](e)s(t) timesClue: [t][i]m[e]s tiger Clue:
[t][i][g][e][r] 
"""

from random import randrange

# set the true word as:
lingo = 'tiger'
while True:
    # let user input the word
    word = input('Guess ')
    # convert str to list
    li_lingo = list(lingo)
    li_word = list(word)
    # if user is correct, print the word and break
    if lingo == word:
        print('[t][i][g][e][r]')
        break
    # if not, we give some clues
    for i in range(len(li_word)):
        # if user gets the right characters and positions, we add a '[]'
        if li_word[i] == li_lingo[i]:
            seq = ('[',li_word[i],']')
            li_word[i] = ''.join(seq)
            print(li_word[i])
        # if user gets the right characters, add a '()'
        elif li_word[i] in lingo:
            seq1 = ('(',li_word[i],')')
            li_word[i] = ''.join(seq1)
    # convert list to str
    clue = ''.join(li_word)
    # print the clue to the user
    print('Clue: ',clue)




print (11)

"""
A sentence splitter is a program capable of splitting a text into
sentences. The standard set of heuristics for sentence splitting
includes (but isn't limited to) the following rules:
Sentence boundaries occur at one of "." (periods), "?" or "!", except
that
a. Periods followed by whitespace followed by a lower case letter
are not sentence boundaries.
b. Periods followed by a digit with no intervening whitespace are
not sentence boundaries. 
c. Periods followed by whitespace and then an upper case letter,
but preceded by any of a short list of titles are not sentence
boundaries. Sample titles include Mr., Mrs., Dr., and so on.
d. Periods internal to a sequence of letters with no adjacent
whitespace are not sentence boundaries (for example,
www.aptex.com, or e.g).
e. Periods followed by certain kinds of punctuation (notably comma
and more periods) are probably not sentence boundaries.
Your task here is to write a program that given the name of a text
file is able to write its content with each sentence on a separate
line. Test your program with the following short text: Mr. Smith
bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't
true... Well, with a probability of .9 it isn't. The result should be:
Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e.
he paid a lot for it. Did he mind?Adam Jones Jr. thinks he
didn't.In any case, this isn't true...
Well, with a probability of .9 it isn't. 

"""

import re
# create a variable text to store text

text = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."
# split sentences in the text and store them into variable sp
sp = re.split('(?<!\w\.\w.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s' , text)

# print the new text
for i in sp :
    print(i + '\n')










