import random
list=[]
for i in range(4):
  nums=random.randint(1,4)
  for j in range(nums):
    list.append(nums)
print (list)
print(len(list))