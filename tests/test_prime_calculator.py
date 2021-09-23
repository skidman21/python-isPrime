import pytest
from prime_calculator import PrimeCalculator


PRIMES_TO_1000 = [
     2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,  53,  59,  61,  67,  71,  73,
     79,  83,  89,  97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
     191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
     311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433,
     439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
     577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
     709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853,
     857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997,
]


PRIME_EXAMPLES = [
    (-10, False), #If a negative # is introduced, can it handle this test case?
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (2.5, False), # How should we handle decimals? Are we handling decimals?
    (3, True),
    (111, False),
    (934, False),
    #("one", False), #Do we handle strings? How should we handle strings?
    #(None,False),   #How do we handle 'None'?
    #("2️⃣", False)
]


NEXT_PRIME_EXAMPLES = [
    (-10,2), #Handling the edge case of a negative number
    (-1,2),
    (0, 2),
    (1, 2),
    (2, 3),
    (2.5, 3), # How should we handle decimals?
    (3, 5),
    (934, 937),
    (1111, 1117),
    #("one",2),
    #(None,2),
    #("1️⃣",2),
]


@pytest.fixture(scope="session")
def calc():
    return PrimeCalculator()


# assertions in a for loop will stop executing after first failure. I used parametrize tests instead.

# def test_is_prime(calc):
#     for n in PRIMES_TO_1000:
#         assert calc.is_prime(n)


@pytest.mark.parametrize("n", PRIMES_TO_1000)
def test_positive_prime_numbers_to_1000(calc, n):
    assert calc.is_prime(n) is True


@pytest.mark.parametrize("n, expected", PRIME_EXAMPLES)
def test_is_prime(calc, n, expected):
    assert calc.is_prime(n) == expected


@pytest.mark.parametrize("n, expected", NEXT_PRIME_EXAMPLES)
def test_next_is_closest_prime(calc, n, expected):
    assert calc.next(n) == expected
