# Part 2 of the Python Review lab.

def encode(x, y):
	if y not in range(1,250) and x not in range(500,1000):
		print("Invalid input: Outside range.")
		return None

def decode(coded_message):
	pass

encode(2,1200)