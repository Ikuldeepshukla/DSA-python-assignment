# given an array with some integer type values. Write a python script to sort these values.

def sortNumbers(nums):
    n = len(nums);

    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1] , nums[j];
    return nums

numsArray = [3,1,4,6,2,4,9,7,0];

print(sortNumbers(numsArray));

