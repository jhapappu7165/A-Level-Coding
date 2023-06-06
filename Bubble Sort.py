num=[0]*5

for i in range (0,5):
    num[i]=int(input("Enter a number = "))

p=0
while p<len(num)-1: #5 numbers mean 4 pass (i.e., 0,1,2,3); len(num)-1 = 4 which means while p<4 [OR, p<=3]

    j=0
    while j<(len(num)-1)-p: #len(num)-1 = 4 which means while j<4-p [OR, j<=3-p]

        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp

        j=j+1
    p=p+1

for k in range(0,5):
    print(num[k])
print(num)
