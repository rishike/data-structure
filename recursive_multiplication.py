

def multipy_recursive(n, a):
	if n == 1:
		return a

	return multipy_recursive(n-1, a) + n


def exp_iterative(a, n):
	base = a
	for i in range(n-1):
		a *= base
	return a

def exp_recursive(a, n):
	if n == 1:
		return a
	else:
		return exp_recursive(a, n-1) * a
