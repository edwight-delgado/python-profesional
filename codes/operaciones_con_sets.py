def union(set_one, set_two):
	# Combinacion de sets
    return set_one | set_two 


def interseccion(set_one, set_two):
	# Interseccion; el resultado de combinar ambos sets, pero solo nos quedamos 
	# con los elementos en comun.
    return set_one & set_two


def diferencias(set_one, set_two):
	# Diferencia; el resultado de tomar dos sets, y remover todo lo que contenga  
	# el segundo set, se arrojan todos los datos del primer set sin los repetidos 
	# con el segundo.
    return set_one - set_two


def diferencia_simetrica(set_one, set_two):
	# Diferencia simetrica; es lo contrario de la interseccion, excepto lo que se  
	# comparte.
    return set_one ^ set_two


def main():
    set_one = {1,2,3}
    set_two = {4,2,5,6}
    print(f'set 1: {set_one} and set 2 {set_two}')
    print()
    print("Union:                ", union(set_one, set_two))
    print("Diferencias:          ", diferencias(set_one, set_two))
    print("Diferencia simetrica: ", diferencia_simetrica(set_one, set_two))
    print("Interseccion:         ", interseccion(set_one, set_two))

    
if __name__ == '__main__':
    main()