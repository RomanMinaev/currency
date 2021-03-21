from datetime import datetime

def read_ints(path):
	lst = []
	with open(path, 'r') as handler:
		while line:=handler.readline():
			lst.append(int(line))
	return lst

def count_three_sum(ints):
	print(f'started {count_three_sum.__name__}')

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
	count_three_sum(ints)
	end = datetime.utcnow()
	print(f'__main__ ended. {end - start}')