# integer declaration
num=10
print(type(num))

# string declaration
str1='string 1'
print(type(str1))
str2="String2"
print(type(str2))
str3='''HI there,
How are you?
Are you doing fine'''
print(type(str3))
print(str3)

'''
hi there this 
is also utilized for multi line comment
'''
# boolen(true/false)
b1=True
b2=False
print(type(b1))
print(type(b2))

# complex (3+9i)(real+imaginary*i(squrt(-1)))
'''
Used to caluclate some records in electronics like power supply
'''
c=12+9j
print(type(c))

# float(Mantise.decimal)
f1=12.59
print(type(f1))
f2=1259e-2
print(f2)
f3=1259e2
print(f3)

# base converstion
b=bin(10)
print(b)
o=oct(10)
print(o)
h=hex(10)
print(h)

# type conversion(transform one data type to another data type)
# implect type convertions 
'''
when we are performing some actions 
the data will be automatically coverted 
'''
a=10
b=2.30
c=a+b
print(c)
boo=True 
print(type(boo))
out=a+boo
print(out)
# explict type converstions
'''
we are forcing a data type to convert into another datatype
by sung some of the bulit-in methods
'''
# int()
# str()
# bool()
# complex()
# float()
a=10
print(float(a))
print(type(float(a)))
print(bool(a))
print(type(bool(a)))
print(str(a))
print(type(str(a)))
print(complex(a))
print(type(complex(a)))

# float
f=12.99
print(int(f))
print(type(int(f)))
print(str(f))
print(type(str(f)))
print(complex(f))
print(type(complex(f)))
print(bool(f))
print(type(bool(f)))

# string
s='name'
print(bool(s))
print(type(bool(s)))
s1='10'
'''
only valued strings can convert into int
'''
print(int(s1))
print(type(int(s1)))
print(complex(s1))
print(type(complex(s1)))
print(float(s1))
print(type(float(s1)))


b=True
print(int(b))
print(type(int(b)))
print(float(b))
print(type(float(b)))
print(complex(b))
print(type(complex(b)))
print(str(b))
print(type(str(b)))

c=10+9j
# print(int(c))
# print(type(int(c))) int()(built-in function can not convert complex into
# intiger)
print(str(c))
print(type(str(c)))
print(bool(c))
print(type(bool(c)))
# print(float(c))
# print(type(float(c)))
