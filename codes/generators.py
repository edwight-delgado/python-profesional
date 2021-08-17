import time

def fibo_gen(max_value=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux
            if max_value!= None and aux > max_value:
                break

if __name__ == '__main__':
    tipo = input('select an option 1-infinite 2-with limit')
    #genrador infinito
    if tipo =='1':
        fibonacci = fibo_gen()
    elif tipo == '2':
        fibonacci = fibo_gen(100)
    else:
        print('invalid option')
        exit()
    #generador con limite
    for element in fibonacci:
        print(element)
        time.sleep(.05)