'''
i=1
while i<=10:
    print(i)
    i+=1
else:
    print('Loop completed')
'''
"""
if 1!=1:
   print('This is a flase statement')
else:
   print('THis is a true statement')   
""" 
'''
for i in range(10,0,-1):
    print(i)
else:
    print('for is also ended')   
'''
'''
for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print(' ')
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print('*',end=' ')
    print('')  
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print('')  
'''  

'''
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print('*',end=' ')
    print('') 
'''

'''
for j in range(1,6):
    print(' '*(5-j)+'* '*j)
'''     

'''
print even numbers form 1 to 100
print how many factors are there for a given number
print wether a number is a prime number or not
print prime numbers from 1 to 100
verify a number is a palendrome
verify the foctorial of a number
print fibbanocci series
01123581321
'''
'''
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,'is a prime number')
'''
'''
num=int(input('Enter the number: '))
fact=1
for i in range(num,0,-1):
    fact*=i
print(fact)
'''
'''
number=int(input('Enter the number: '))
a=0
b=1
for i in range(1,number+1):
    print(a,end=',')
    c=a+b
    a=b
    b=c
'''
'''
A
A B
A B C
A B C D
A B C D E

A
B C
D E F
G H I J
K L M N O
'''    

'''
65-90
97
'''
'''
count=65
for i in range(65,70):
    for j in range(65,70):
        if i>=j:
            print(chr(count),end=' ')
            count+=1
            
    print(' ')        
'''

year=int(input('Enter the Year :'))
if year%100==0:
    if year%400==0:
        print(year,'is a leap year')
    else:
        print(year,'is not a leap year')
elif year%4==0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')                  
    
   
        
               