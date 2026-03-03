'''
sen='HI there!
How are you?
i am doing grate
'
print(sen)
# immutable
s='Hi'
print(id(s))
s='Hello'
print(id(s))
print(s)
# splicing
str1='madam'
str2=str1[0:len(str1):2]
print(str2)
str3=str1[::-1]
print(str3)
str4=str1[:str1.find('d')+1:1]
print(str4)
# travers
for i in range(0,len(str1)):
    print(str1[i])

for i in str1:
    print(i)
'''
#searching meathods: 

str1='some string'
# find: return the index position of sub string. it is going to give
# first occrance, we can also change the position of finding by giving index
# if sub string is not available in the string then it is going to retun -1
print(str1.find('d',1,3))
print(str1.rfind('s'))
print(str1.index('s'))
# it is going to through an error if the sub-string is not available
print(str1.rindex('s'))

# counting methods:
print(str1.count('s'))

# formatting methods:
# ljust
print(str1.ljust(len(str1)+6,'$'))

