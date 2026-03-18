# creation tuple
'''
t=(1,2,3,4,5)
print(type(t))
t1=('james',24,'hyd','s/w eng',[1,2,3,4])
print(type(t1))
t2=tuple([1,2,3,4,5])
print(t2)
t3=(3,)
print(type(t3))
# packing of a tuple
t4=10,20,30,40
print(type(t4))
t5=tuple('python')
print(t5)
# upacking of tuple
a,b,c,d=t4
print(a)

# reading values from a tuple
print(t4[0])

#immutable
# t4[0]=50

# how to traves through a tuple
for i in t5:
    print(i)
'''
# genarator tuple creation
'''
t1=tuple((x**2 for x in range(1,6)))
print(t1)

# Advance concept
# genarator + upacking of a tuple
t2=(*(x**2 for x in range(1,6)),)
print(t2)

# indexing as splicing but only for reading purpose
t3=t2[0:3:1]
print(t3)
print(t3[-1])
'''
#concatination of tuple
# t1=(1,2,3,4,5)
# t2=(6,7,8,9,10)
# t3=t1+t2

# print(t3)

# repetaion of a tuple
# t1=(1,2,3)
# t2=t1*3
# print(t2)
