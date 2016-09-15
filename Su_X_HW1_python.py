# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:19:15 2016

@author: sxq
"""

#Group C&D

print (1)
"""
Represent a small bilingual lexicon as a Python dictionary in the following 
fashion {"merry":"god", "christmas":"jul","and":"och","happy":gott",
"new":"nytt","year":"år"}and use it to translate your Christmas cards 
from English into Swedish. That is, write a function translate()that 
takes a list of English words and returns a list of Swedish words. 

"""
# We first input te regular expression operations in python, which would 
# helpful for us to coding.
import re
re.compile('<title>(.*)</title>') 


# We define a dictionary that includes the English words and corresponding 
# Swedish words.
 
dict = {"merry":"god",
        "christmas":"jul",
        "and":"och",
        "happy":"gott",
        "new":"nytt",
        "year":"år"}
        
# We define a function translate(inpString) to translate the "String" we 
# input in English to the corresponding Swedish words we just defined above.
# Notice that the "inpString" in the parenthesis of the function translate()
# is the "String" readers could input themselves. 
        
def translate(inpString):
    # define a term
    translatedString = ""
     
    #let the python reads every characters in the ""
    for i in inpString.split(" "):
        # Here we have to consider two situations, one is there is no
        # characters in the "", i.e, the inpString is empty, and another 
        # situation is that there are characters in the inpString.
    
        if (str(dict.get(i))) != "None":# the inpString is not empty
            # We translate the inpString by using the dictionary we defined 
            # above, and store the translated string into the 
            # "translatedString"
            translatedString = translatedString+str(dict.get(i))+" "
        # the inpString is empty    
        else:
            translatedString = ""
            # simply return the ""
            return translatedString
             
    return translatedString
             
# we test the function translate()
             
print(translate("merry christmas and happy new year"))
print(translate("happy new year"))
print(translate(""))

print (2)
    
"""

Write a function char_freq()that takes a string and builds a
frequency listing of the characters contained in it. Represent 
the frequency listing as a Python dictionary. Try it with something 
like char_freq("abbabcbdbabdbdbabababcbcbab"). 

"""
# We define the function char_freq()that takes a string    
def char_freq(string):
  # define the term freq
  freq = {}
  # we let the python read the string in the function char_freq()
  for i in string:
    # We count the frequency of each characters in the string,  
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1
  return freq
      
# we test the function char_freq()
print (char_freq("abbabcbdbabdbdbabababcbcbab"))


print(3)

"""

In cryptography, a Caesar cipher is a very simple encryption
techniques in which each letter in the plain text is replaced by a 
letter some fixed number of positions down the alphabet. For example, 
with a shift of 3, A would be replaced by D, B would become E, and 
so on. The method is named after Julius Caesar, who used it to communicate 
with his generals. ROT-13 ("rotate by 13 places") is a widely used example 
of a Caesar cipher where the shift is 13. In Python, the key for ROT-13 
may be represented by means of the following dictionary: key = {'a':'n', 
'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 
'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 
'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j','x':'k', 'y':'l', 
'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q','E':'R', 'F':'S', 'G':'T', 
'H':'U', 'I':'V', 'J':'W', 'K':'X','L':'Y', 'M':'Z', 'N':'A', 'O':'B', 
'P':'C', 'Q':'D', 'R':'E','S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 
'X':'K', 'Y':'L','Z':'M'} Your task in this exercise is to implement 
anencoder/decoder of ROT-13. Once you're done, you will be able to read 
the following secret message: Pnrfne pvcure? V zhpu cersre Pnrfne fnynq! 
Note that since English has 26 characters, your ROT-13 program will be 
able to both encode and decode texts written in English. 

"""

#Algorithm
#Split the sentence into words
#Split the words in to letters
#Use the letters to search in the dictionary
#Create new words from the letters and sentence from words
 
import re
# we create the key of the ROT-13 as reference
 
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 
       'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 
       'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 
       'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 
       'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 
       'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 
       'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 
       'X':'K', 'Y':'L', 'Z':'M'}
# We define a function that includes the cryptogram that needs to be decoded
# and encoded 

def dec_enc(inpString):
    # define a term for storing the string
    newString = ""
    
    # print the string first for reference 
    print(inpString)
    
    # let the function reads the words in inpString

    for word in inpString:
        # we want to encode and decode the characters of the words 
        # in string one by one
        for i in range(len(word)):
            # we decode or encode the string
            if word[i] in key:
                newString = newString+key[word[i]]
            # for punctuation
            else:
                newString = newString+word[i]
        # we add a space at the end of each word for readability.
        newString = newString+" "
    print(newString)
 
# we test the function dec_enc            
 
dec_enc("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")
 
print("\n")
 
dec_enc("Caesar cipher? I much prefer Caesar salad!")


print (4)

"""
Define a simple "spelling correction" function correct()that takes a
string and sees to it that 1) two or more occurrences of the space
character is compressed into one, and 2) inserts an extra space
after a period if the period is directly followed by a letter. E.g.
correct("This is very funny and cool.Indeed!")should return
"Thisisveryfunnyandcool.Indeed!"Tip: Use regular expressions! 

"""
import re
# We define a function correct() that includes a string.

def correct(str):
  # we use re.sub to sustitute the two spaces into one.
  compressed = re.sub(r'\s{2,}', ' ', str)
  # similarly, we use re.sub to insert a space after a period.
  insert = re.sub(r'(\.)(\w)', r'\1 \2', compressed)
  return insert

# we test the function correct()
print(correct('This   is        very funny  and    cool.Indeed!'))


print (5)
"""
The third person singular verb form in English is distinguished by
the suffix -s, which is added to the stem of the infinitive form: run ->
runs. A simple set of rules can be given as follows: a. If the verb
ends in y, remove it and add ies b. If the verb ends in o, ch, s, sh, x
or z, add es c. By default just add s Your task in this exercise is to
define a function make_3sg_form()which given a verb in infinitive
form returns its third person singular form. Test your function with
words like try, brush, run and fix. Note however that the rules must
be regarded as heuristic, in the sense that you must not expect
them to work for all cases. Tip: Check out the string method
endswith(). 

"""
# we define a term suffixes to store the special suffixes.
suffixes = ('o', 'ch', 's', 'sh', 'x', 'z')
# we define a function make_3sg_form() which given an infinitive form 
# of a verb returns its third person singular form 
def make_3sg_form(verb):
  # there are three situations, the verb ends with "y",
  if verb.endswith('y'):
    return verb[:-1]+'ies'
  # the verb ends with special suffixes
  elif verb.endswith(suffixes):
    return verb+'es'
  # other
  else:
    return verb+'s'

#we test the function make_3sg_form

print(make_3sg_form('try'))
print(make_3sg_form('brush'))
print(make_3sg_form('run'))
print(make_3sg_form('fix'))

print (6)

"""
In English, the present participle is formed by adding the suffix -ing
to the infinite form: go -> going. A simple set of heuristic rules can
be given as follows:
a. If the verb ends in e, drop the e and add ing (if not exception: be,
see, flee, knee, etc.) b. If the verb ends in ie, change ie to y and
add ing c. For words consisting of consonant-vowel-consonant,
double the final letter before adding ing d. By default just add ing
Your task in this exercise is to define a function
make_ing_form()which given a verb in infinitive form returns its
present participle form. Test your function with words such as lie,
see, move and hug. However, you must not expect such simple
rules to work for all cases. 

"""
# create a term vowels to store all vowels

vowels = 'aeiou'
# We define a function make_ing_form() which given an infinitive form 
# of a verb returns its present participle form
def make_ing_form(verb):
  # there are four situations, the verb ends with "ie"
  if verb.endswith('ie'):
    return verb[:-2]+'ying'
  # the verb ends with "e"
  elif verb.endswith('e'):
    return verb[:-1]+'ing'
  # the verb ends in a form of "consonant-vowel-consonant"
  elif verb[-3] not in vowels:
    if verb[-2] in vowels:
      if verb[-1] not in vowels:
        return verb+verb[-1]+'ing'
  # default
  else:
    return verb+'ing' 

# we test the function make_ing_form()
print(make_ing_form('lie'))
print(make_ing_form('see')) 
# the function here does not work, because "see" is an exception.
print(make_ing_form('move'))
print(make_ing_form('hug'))



print (7)
"""
Using the higher order function reduce(), write a function
max_in_list()that takes a list of numbers and returns the largest
one. Then ask yourself: why define and call a new function, when I 
can just as well call the reduce() function directly? 

"""
# bring in the function tools in python 
from functools import reduce

# we define a function max_in_list() that takes a list of numbers and 
# returns the largest one.

def max_in_list(num):
  # we use lambda here to replace a function, thus simplifying the process
  return reduce(lambda x, y: x if x > y else y, num)

#we test the function max_in_list()
print(max_in_list([1,9,6,8,11,22]))

# we define a function here, and then we could directly input the list
# of numbers. If we use reduce(), the process of finding the maximum value
# in a list would be much more redundant 

print (8)

"""
Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words. Write it in
three different ways: 1) using a for-loop, 2) using the higher order
function map(), and 3) using list comprehensions. 

"""


# We define a function len_words() that maps a list of words into a list of
# integers representing the lengths of the corresponding words. 
# we use three methods
# we use a for-loop
def len_words_one(words):
  
  wordsLength = []
  for word in words:
    wordsLength.append(len(word))
  return wordsLength

# we use the higher order function map()
def len_words_two(words):
  return list(map(len, words))
  
# we use the list comprehensions
def len_words_three(words):
  return [len(word) for word in words]

# We test the function
print(len_words_one(['happy', 'new', 'year']))
print(len_words_two(['happy', 'the', 'Mid', 'August', 'festival']))
print(len_words_three(['Bonjour', 'Salut', 'Ca va', 'Merci']))


print (9)

"""

Write a function find_longest_word()that takes a list of words
and returns the length of the longest one. Use only higher order
functions. 

"""
# We define a function find_longest_word()that takes a list of words
# and returns the length of the longest one

def find_longest_word(words):
  # we list the lengths of each words we input 
  return max(list(map(len, words)))

#we test the function
print(find_longest_word(['hello', 'fabulous', 'probability']))


print (10)

"""
Using the higher order function filter(), define a function
filter_long_words()that takes a list of words and an integer
and returns the list of words that are longer than n.

"""
# We define a function
#filter_long_words()that takes a list of words and an integer
#and returns the list of words that are longer than n.

def filter_long_words(words, n):
    
  return [x for x in words if len(x) > n]

# We test the function
print(filter_long_words(['hello', ' world', 'happy', 'new', 'year'], 4))


print (11)

"""
Represent a small bilingual lexicon as a Python dictionary
in the following fashion {"merry":"god",
"christmas":"jul","and":"och","happy":gott","new":"nytt","y
ear":"år"}and use it to translate your Christmas cards from
English into Swedish. Use the higher order function map()to write
a function translate() that takes a list of English words and
returns a list of Swedish words. 

"""
            
# We create a disctionary that includes the English words and 
# corresponding Swedish words                 
dict = {"merry":"god", "christmas":"jul", "and":"och",\
        "happy":"gott", "new":"nytt", "year":"år"}
        
# We define a function translate() to translate English into Swedish.   
def translate(words):
	return map(lambda x: dict[x.lower()], words)

#we test the function 
print (translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year']))

print (12)

"""

Implement the higher order functions map(), filter()and
reduce(). (They are built-in but writing them yourself may be a
good exercise.) 

"""

#help('map')
#help('filter')
#help('reduce')
# We define a function map()
def map(function, sequence):
  result = []
  for item in sequence:
    result.append(function(item))
  return result

# We define a function filter()
def filter(function, sequence):
  # If sequence is a tuple or string, return the same type, 
  # else return a list.
  if isinstance(sequence, tuple):
    result = ()
  elif isinstance(sequence, str):
    result = ''
  else:
    result = []
    
  for item in sequence:
    if function(item):
      # Add the item according to the type of sequence
      if isinstance(sequence, tuple):
        result += (item,)
      elif isinstance(sequence, str):
        result += item
      else:
        result.append(item)
  return result

# We define a function reduce() 
def reduce(function, sequence, initial=None):
  # We set the initial to NONE 
  result = initial if initial else sequence[0]
  if initial:
    for item in sequence:
      result = function(result, item)
  else:
    for item in sequence[1:]:
      result = function(result, item)
  return result

# we test these functions
print (list(map(lambda x: x * 3, [1,2,3,4])))
print (list(filter(lambda x: x.endswith('in'), ('sigma', 'pin', 'none'))))
print (reduce(lambda x, y: x+y, [1, 2, 3, 4], 6))





