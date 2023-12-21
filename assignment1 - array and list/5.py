# Write a Python script to create a list of first N terms of a Fabonacci series.

def getFabonacciSeries(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = getFabonacciSeries(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

    
print(getFabonacciSeries(5))