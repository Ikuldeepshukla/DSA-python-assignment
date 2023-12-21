# Write a Python script to create a list of first N prime numbers.

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    """Return a list of the first n prime numbers."""
    primeNumbers = []
    number = 2  # Start with the first prime number
    while len(primeNumbers) < n:
        if is_prime(number):
            primeNumbers.append(number)
        number += 1
    return primeNumbers

print(getPrimeNumbers(10))
