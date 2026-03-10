'''
string:string is noting but combination of group of charaters 
which are represted in an array
list=[]we can add elements in a hetrogenious way
array=[]we can add hemoginous values
'''

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

# str1='some string'
'''
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
'''
'''
# formatting methods:
# ljust
print(len(str1))
print(len(str1.ljust(len(str1)+6,' ')))
# rjust
print(str1.rjust(len(str1)+5,'$'))
# center
print(str1.center(len(str1)+9,'$'))
# zfill
print(str1.zfill(len(str1)+6))
'''
# trim
# str1='Hi world     '
# print(str1.lstrip())
# print(str1.rstrip(),'$')
# print(str1.strip())

# joins and spilts
# replace
'''
str1='Hi world'
print(str1.replace('Hi','Hello'))
# join
str2='abc'
str3='/'
print(str3.join(str2))
'''
# split:
# s1='Hi john How are you'
# print(s1.split(' ',1))
# print(s1.rsplit(' ',1))
# s2='''Hi there!
# how are you
# i am doing fine
# hope you are doing grate
# '''
# print(s2.splitlines())

# prefix and sufix
# stratswith
# s1="Hi hello world"
# print(s1.startswith('HI'))
# endswith
# print(s1.endswith('ld'))

# s1='Hi Hello World'
# print(s1.removeprefix('Hi'))
# print(s1.removesuffix('ld'))
# print(s1.partition(' '))

# email='somename@gmail.com'
# print(email.partition('@'))

# styles
name='aeiouAEIOU'
print(name.lower())
print(name.upper())
print(name.casefold())
print(name.swapcase())

mname='the man with golden gun'
print(mname.capitalize())
print(mname.title())

num='12'
print(num.isalnum())
f='12'
print(f.isdecimal())
s=' '
print(s.isspace())
aln='abc123'
print(aln.isalnum())
l='aeiou'
print(l.isalpha())
print(l.islower())
u='AEIOU'
print(u.isalpha())
print(u.isupper())


print(isinstance(12,int))




