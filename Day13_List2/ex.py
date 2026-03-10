# list contanitation
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=l1+l2
# print(l3)
# l4=l1*3
# print(l4)

# membership oparators (in, not) list verfication of elements
# print(5 in l1)

# list comarisions
# l1=[1,6,3,4]
# l2=[1,2,3]
# print(l2>l1)

# l1=['apple','bananna','cat']
# l2=['dog','elephant','flag']
# print(l2>l1)
# print(ord('d'),ord('a'))

# traverse:how can travel through the list
# l1=[1,2,3,4,5,6,7,8,9,10]
# for i in l1:
#     print(i)

# for i in range(0,len(l1)):
#     print(l1[i])

# methods of list
# Adding element methods of list
'''
append
extend
insert
copy()
'''
# l1=[1,2,3,4]
# l1.append(5)
# print(l1)
# l1.extend((6,7,8,9))
# print(l1)
# l1.insert(0,10)
# print(l1)
# l2=l1.copy()
# print(l2)
# print(id(l1))
# print(id(l2))
# l3=l1
# print(id(l3))
# print(id(l1))

# removing methods of a list
'''
pop
remove
clear
del
'''
# l1=[1,2,3,4,5,6]
# l1.pop()
# print(l1)
# l1.append(5)
# print(l1)
# l1.remove(5)
# print(l1)
# l1.remove(5)
# print(l1)
# l1.clear()
# print(l1)
# del(l1)
# print(l1)

# index,sort,reverse
# index
'''
index
count
'''
# l1=[1,2,3,4,5,3]
# print(l1.index(3))
# print(l1.count(3))

# reverse
# l1=[1,2,3,4,5]
# l1.reverse()
# print(l1)

# sort
# l1=[70,10,30,50,40,60,20]
# l1.sort(reverse=True)
# print(l1)

# l1=[]
# for i in range(10,110,10):
#     l1.append(i)

# print(l1)

# list comprahenssion
'''
l1=[x*10 for x in range(1,11)]
'''
# l1=[x*10 for x in range(1,11)]
# print(l1)

# l1=[x**3 for x in range(1,11)]
# print(l1)

# l1=[x.lower() for x in 'PYTHON']
# print(l1)

# l1=[int(x) for x in '0123456789']
# print(l1)

l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
for i in l1:
    for j in i:
        print(j,end=' ')
    print('')  

# for i,j in l1,l2:
#     print(i+j)






