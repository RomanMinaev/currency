from datetime import datetime
import threading
from functools import wraps

def timer(func):
	@wraps(func)
	def wrap(*args, **kwargs):
		start = datetime.utcnow()
		output = func(*args, **kwargs)
		end = datetime.utcnow()
		print(f'{func.__name__} took {end-start} to run.')
		return output
	return wrap

def read_ints(path):
	lst = []
	with open(path, 'r') as handler:
		while line:=handler.readline():
			lst.append(int(line))
	return lst

@timer
def count_three_sum(ints):
	print(f'Starting {count_three_sum.__name__}')

	n = len(ints)
	counter = 0

	for i in range(n):
		for j in range(i+1, n):
			for k in range(j+1, n):
				if ints[i] + ints[j] + ints[k] == 0:
					counter += 1
					print(f'Triple found {ints[i]} | {ints[j]} | {ints[k]}', end='\n')

	print(f'Function {count_three_sum.__name__} closed. Counter = {counter}')



if __name__ == '__main__':
	print('Starting __main__')

	start = datetime.utcnow()
	ints = read_ints(r'for_thread_test/1Kints.txt')

	t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
	t1.start()
	print('Counter is in thread. __main__ loop continues...')
	end = datetime.utcnow()
	t1.join()
	true_end = datetime.utcnow()
	print(f'__main__ ended. {end - start}\n'
		f'__main__ TRULY ended at {true_end - start}')