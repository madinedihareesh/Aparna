# set:{}
# creation methods for sets:
# it can hold homoginous type of elements
# it won't allow duplicate elements
# it is not having index or sequenctional data
# s={1}
# print(type(s))
# s1={10,'james',[1,2,3,4]}
# print(s1)
# s1=set()
# print(type(s1))
# s2=set('python')
# print(s2)
# travsing thought sets
# for i in s2:
#     print(i)

#mutable
# s2.add('s')
# print(s2) 
# s2.add('s')
# print(s2)


# a={1,2,5,6,7}
# b={6,7,8,9,11}
'''
# mathamatical methods
# union:
res=a.union(b)
print(res)

# intersection:
res1=a.intersection(b)
print(res1)

# diffrence
res2=a.difference(b)
print(res2)

# sematic diffrence:
res3=a.symmetric_difference(b)
print(res3)

# intersection_update
# diffrence_update
# sematic_diffrence_update
a.symmetric_difference_update(b)
print(a)
'''
# oparators
'''
| uniuon
& intersection
&= intersection_update
-  diffrence
-= diffrence_update
^ sematric_diffrence
^= semaritc_diffrence_update
'''
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)

# methods for sets
# s1={1,2,3,4,5,6}

# adding methods
'''
add
update
'''
# s1.add(7)
# print(s1)
# s1.update((8,9,10))
# print(s1)

# deleteing elements
# s1.remove(5)
# print(s1)
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)
# del(s1)
# print(s1)

# set comprahenssions
# s1={x for x in range(1,6)}
# print(s1)
