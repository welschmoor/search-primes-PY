

def isPrime(num):
	for each in range(2, num):
		if num%each == 0:
			return False
	return True


def createPrimeList(upToNum):
	for each in range(2, upToNum):
		if isPrime(each):
			list_of_primes.append(each)


list_of_primes = [];
print(isPrime(7))

createPrimeList(100)
print(list_of_primes)
