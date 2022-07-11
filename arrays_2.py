###this programme asks the user to enter an array of 5 integers and is displayed in reverse order
from array import *
nums=array('i',[])
for x in  range(0,5):
     num=int(input('enter values: '))
     nums.append(num)
nums=sorted(nums)
print(nums)
nums.reverse()
print(nums)



















