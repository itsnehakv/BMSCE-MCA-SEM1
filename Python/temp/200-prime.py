# Write a program to find sum of prime numbers till 200
sum=0
for num in range(1,201):
    count=0;
    for i in range(1,num+1):
        if(num%i==0):
            count+=1

    if (count==2):
        sum+=num

print("Sum of 1st 200 prime numbers:",sum)
