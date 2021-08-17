#hola 3 -> holaholahola 
#edwight 2 -> edwightedwight
#platzi 4 -> platziplatziplatziplatzi

def make_repeater_of(n):
	def repeater(string):
		assert type(string) == str,"solo puedes usar string"
		return string * n

	return repeater


def main():
	repeat_5 = make_repeater_of(5)
	print(repeat_5('hola'))

if __name__ == '__main__':
	main()