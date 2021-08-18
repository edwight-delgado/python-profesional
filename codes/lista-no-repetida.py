
lista = [1,2,2,3,3,4]
lista2 = ['edwight','diana','maria','juan','diana','maria','juan']
def remove_duplicate(lista,method=1):
	if method==1:
		delete_repeated_items=[]
		for value in lista:
			if value not in delete_repeated_items:
				delete_repeated_items.append(value)
		return delete_repeated_items
	elif method==2:
		return list(set(lista))

def main():
	for x in [lista,lista2]:
		no_duplicate_list=remove_duplicate(x,2)
		print('original list {} , list without duplcate {}'.format(x,no_duplicate_list))

if __name__ == '__main__':
	main()