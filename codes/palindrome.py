def is_palindrome(string:str)->bool:
	"""Returns if the string is palindrome (True or False)"""
	string= string.replace(" ","").lower()
	return string == string[::-1]

def suma(a:int,b:int)->int:
	return a+b

def main():
	print(suma('2','3'))
	#lista =[ (value ,is_palindrome(value)) for value in ['Ana','Maria','oro','ala',1000]]
	#print(lista)
	print(is_palindrome(1000))

if __name__ == '__main__':
	main()