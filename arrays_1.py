from array import*
nums=array('i',[79,13,23,45,67,87,98])
print(nums)
for x in nums:
    print(x)
newvalue=int(input('enter number: '))
nums.append(newvalue)
print(nums)
nums.reverse()
print(nums)
nums=sorted(nums)
print(nums)
nums.pop()
print(nums)

newarray=array('i',[])
more=int(input('how many values: '))
for a in range(0,more):
    newvalue=int(input('enter number: '))
    newarray.append(newvalue)
nums.extend(newarray)
getrid=int(input('enter index of item: '))
newarray.remove(getrid)
print(nums)

