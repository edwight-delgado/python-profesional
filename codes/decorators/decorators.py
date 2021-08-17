from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
    return wrapper

def mayuscula(func):
	def wrapper(*args,**kwargs):
		return func(*args).upper()
	return wrapper

@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass

@execution_time
def suma(a,b):
	print(a+b)

@mayuscula
def texto(string):
	return string

print(texto('esto es un ejemplo'))


#suma(3,5)
random_func()