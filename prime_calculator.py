import math
import sys

class PrimeCalculator:

	@staticmethod
	def next(value: int) -> int:
		test = value + (2 if (value % 2 == 1) else 1)
		while not PrimeCalculator.is_prime(test):
			test += 2
		return test

	@staticmethod
	def is_prime(value: int) -> bool:
		if value == 2:
			return True
		# Check if the value is even
		if value % 2 == 0:
			return False
		value2 = [
			i for i in range(2, int(math.sqrt(value)))
			if i % 2 != 0
		]
		for v in value2:
			if value % v == 0:
				return False
		return True



if __name__ == "__main__": # pragma nocover
    number = int(sys.argv[1])
    prime = PrimeCalculator().next(number)
    print(f"Next Prime: {prime}")
