# ways for creation of list:
'''
l1=[1,2,3,4,5,1]
print(l1)
print(type(l1))
l2=list((1,2,3,4))
print(l2)
print(type(l2))
l3=list('Python')
print(l3)
l4=[]
print(type(l4))
'''
'''
List: List is a mutable ordered collection of elemnts 
which acctepts Hetrogenious values as well as duplicates

'''
'''
l5=[21,12.59,True,10+11j,'james']
print(l5)
print(type(l5))

print(l1[1])
print(id(l1))

l1[0]=10
print(l1)
print(id(l1))
'''
# splicing:
l1=[1,2,3,4,5,6]
#   0 1 2 3 4 5 6
l1[0:0]=[10]

print(l1)
l1[0]=11
print(l1)
l1[0:2]=[10]
print(l1)
l1[2:3]=[11]
print(l1)
l1[9:9]=[12]
print(l1)
l1[:]=[13,14,15]
print(l1)
l1[::-1]=[1,2,3]
print(l1)



