#ITERABLES - an obj that can return its elemnts one at a time
#          allowing it to be iterated over in a loop

#iterate forward
nums = [1,2,3,4,5]
for n in nums:
    print(n, end=" ")  #end=" " - space

#iterate backwards
nums = [1,2,3,4,5]
for num in reversed(nums):
    print(num, end=" ")