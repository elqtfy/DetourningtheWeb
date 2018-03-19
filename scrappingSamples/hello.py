name = "yyyyy"
age = 67
weight = 182.7
is_cool = True
is_cool = False

print "my name is " + name + "I am " + str(age) + " years old. "

a_list = []
a_list.append("the first thing")
a_list.append("the second thing")
a_list.append("the third thing")
a_list.append("the fourth thing")
a_list.append("the fifth thing")
a_list.append("the sixth thing")


#print a list, -1 returns the last one ... -2 -3 in the same way
#print a_list[2:6] 

# for item in a_list:
# 	print item #blank, tab matters 

some_numbers = [100, -500, 200, 1, 7, -1000000, 204]
# for number in some_numbers:
# 	print number
# 	if number>0:
# 		print 	"the number is bigger than 0."
# 	else:
# 		print "that number is less than 0!"

import random

def say_hi(name):
	greeting =  "Hello " + name + "!!!!" 
	return greeting

print say_hi("Karl Marx")

#print dir(random) #showing the whole module/func that random library has

print random.randint(4,60)

