
  

arr=[]
n= int(input("enter the total elements:"))
print("enter the numbers you want to calculate:")
for i in range(n):
    el = int(input())
    arr.append(el)
    
print(arr)


def cal(arr):
    a=0
    for i in range(len(arr)):
        a=a+arr[i]
    return a

s=(cal(arr))
print(s)

a=int(input("enter the total elements:"))
print("enter the numbers to didvide:")

a=int(input())
b=int(input())
div= a/b
print(div)



