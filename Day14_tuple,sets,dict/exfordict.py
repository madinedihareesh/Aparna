# # creation of dict
# d={}
# print(type(d))
# d1={'name':'james','age':20,'value':10+9j,'alive':True,'l1':[1,2,3]}
# print(d1)
# l1=['name','age','loc']
# l2=['james',24,'Hyd']
# d2=dict(zip(l1,l2))
# print(d2)

# t=(('name','james'),('age',24),('loc','hyd'),(0,20))
# d3=dict(t)
# print(d3)

# l3=['one','two','three']
# d4=dict(enumerate(l3,start=101))
# print(d4)
# # key method
# k=d3.keys()
# for i in k:
#     print(d3[i])

# # values method
# v=d3.values()
# for i in v:
#     print(i)

# # items
# i=d3.items()
# print(i) 

# # get
# res=d3.get('name')
# print(res)

# # update
# d4={'job':'S|w Eng'}
# d3.update(d4)
# print(d3)

# # copy
# d5=d3.copy()
# print(id(d3))
# print(id(d5))

# # pop
# # d3.pop('job')
# # print(d3)

# # popitem
# d3.popitem()
# print(d3)
# d3.popitem()
# print(d3)

# # clear
# d3.clear()
# print(d3)

# # del
# del(d3)
# print(d3)

# dict comprohenssion
l1=[('one',1),('two',2),('three',3)]
d1={x:y for x,y in l1}
print(d1)

l2=['one','two','three']
l3=[1,2,3]
d2={x:y for x,y in zip(l2,l3)}
print(d2)

l4=['one','two','three']
d3={x:y for x,y in enumerate(l4,start=1)}
print(d3)