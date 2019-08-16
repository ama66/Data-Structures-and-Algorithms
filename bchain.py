## This is python source code 
import functools
import operator 

simple_list=[1,2,3,4]

def multiply(el):
	return el*2 

####################
print(list(map(multiply,simple_list)))
print(list(map(str,simple_list)))
## Lambda oneliners>>> lambda x,y,z : f(x,y,z)  (inline syntax! )
print(list(map(lambda el: 2*el , simple_list)))
###

# The reduce() function accepts a function and a sequence and returns a single value calculated as follows:

# Initially, the function is called with the first two items from the sequence and the result is returned.
# The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.

# 

def do_sum(x1, x2): return x1 + x2

print(functools.reduce(do_sum, [1,2,3,4]))

print(functools.reduce(do_sum, [1,2,3,4]))

# using reduce to compute sum of list 
lis = [ 1 , 3, 5, 6, 2] 
print("The sum of the list elements is : ") 
print(functools.reduce(lambda a,b : a+b,lis)) 
  
# using reduce to compute maximum element from list 
print("The maximum element of the list is : ") 
print(functools.reduce(lambda a,b : a if a > b else b,lis)) 

print ("The sum of the list elements is : ") 
print (functools.reduce(operator.add,lis)) 

print ("The product of list elements is : " ) 
print (functools.reduce(operator.mul,lis)) 


# using reduce to concatenate string 
print ("The concatenated product is : ") 
print (functools.reduce(operator.add,["geeks","for","geeks"])) 

print ("The summation of list using reduce is :") 
print (functools.reduce(lambda x,y:x+y,lis)) 


a=[1,2,4]
print('some text: {} , {}, {}'.format(*a))

## you can unpack dictionary with two ** 
def nmy_funct(*args, **keywordargs):
	print(keywordargs)
	for arg in keywordargs:
		print(arg, keywordargs[arg])
nmy_funct(1,2,3, name='too', age=29)


