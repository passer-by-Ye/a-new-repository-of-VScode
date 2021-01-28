nums=[]


n1=eval(input("the first number:"))
n2=eval(input("the second number:"))
n3=eval(input("the third number:"))

nums.append(n1)
nums.append(n2)
nums.append(n3)
print(nums)

def findmax():
 if nums[0]>=nums[1] and nums[0]>=nums[2]:
     print(nums[0])
 elif nums[1]>=nums[2]:
     print(nums[1])
 else:
     print(nums[2])

findmax()
findmax()




