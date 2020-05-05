"""
This program is to :
    1.cover all the numeric data types in python
    2.converting from one type to another
    3.generate a random number/element using module "random"

"""

import random

x = 1       #int initialization
y= 2.48     #float initialization
z= 5+2j     #complex initialization

#Note: complex number cannot be converted to any other data type
#uncomment the variable e conversion to check the error

a = int(y)      #float-->int
b = float (x)   #int -->float
c = complex(x)  #int-->complex
d = complex(y)  #float-->complex
#e = int(z)     #complex-->int not supported


print ("a : ", a," is of type : ",type(a))
print ("b : ", b," is of type : ",type(b))
print ("c : ", c," is of type : ",type(c))
print ("d : ", d," is of type : ",type(d))

print(range(0,100))

#generate a  integer random number 

#generate random integer in range(0,100+1)
rand_int = random.randint(0,100)
print ("rand_int : ", rand_int," is of type : ",type(rand_int))

#generate random integer in range(0,100)
rand_int_range = random.randrange(100)
print ("rand_int_range : ", rand_int_range," is in between 0 & 100 and of type : ",type(rand_int_range))

#generate random integer in range(0,100,2) with step 2 -->even number between (0,101)

rand_int_range = random.randrange(0,101,2)
print ("rand_int_range : ", rand_int_range," is in between 0 & 100 with step 2 and of type : ",type(rand_int_range))


#generate a  float random number 

#generate random float in range(0,1) --> [0,1)
rand_float_default = random.random()
print ("rand_float_default : ", rand_float_default," is in between 0 & 1 and of type : ",type(rand_float_default))

#generate random float in range(2.5,100)-->[2.5,100.0)
rand_float_range = random.uniform(2.5,100)
print ("rand_float_range : ", rand_float_range," is in between 2.5 & 100 and of type : ",type(rand_float_range))

#select a random element from a list 
rand_chioce = random.choice(['win','lose','draw'])  
print ("rand_chioce : ", rand_chioce," is in list and of type : ",type(rand_float_range))

#shuffle a list random fashion 
deck = 'ace two three four'.split()
print ("deck before shuffling ")
print(deck)
random.shuffle(deck)
print ("deck after shuffling ")
print(deck)


#get a sample out of a list/any data set 
list_samplea = random.sample([10,20,30,40,50,60,70,80],k=4)
print ("list_samplea : ")
print(list_samplea)
list_sampleb = random.sample([10,20,30,40,50,60,70,80],k=4)
print ("list_sampleb : ")
print(list_sampleb)