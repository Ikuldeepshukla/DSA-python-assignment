# Write a Python script to calculate average of elements of a list.

def getAverage(nums):
    count = 0;
    totalSum = 0;
    for index in range(len(nums)):
        if isinstance(nums[index], int):
            count += 1
            totalSum += nums[index]
    return totalSum / count

demoNums = [1,2,3,4,5,6,7]

print(getAverage(demoNums))