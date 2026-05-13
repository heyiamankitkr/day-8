#to make -ve numbers of list into 0 and keep rest same 
nums=[-2,-3,-7,8,11,12]
nums=[0 if val<0 else val for val in nums]
print(nums)
#capitalising strings
words=["hello","hya","what"]
words=[i.upper() for i in words]
print(words)