# Part 1 of the Python Review lab.

def hello_world():
	return "hello_world"

def greet_by_name(name):

	return "hello" +name 


def encode(x):
	return x*3953531

def decode(y):
	return y/3953531.0

a = 5
a = encode(a)
print(a)
a = decode(a)
print(a)