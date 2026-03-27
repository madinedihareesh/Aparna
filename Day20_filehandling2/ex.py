'''
r read
w write
a append
x creation
r+ read and write
w+ write and read
a+ append and read

pointer 0 1 2 seek()
'''
data='''
hi there hello world
how are youd doing
i am doing fine
'''
# f=open('theory.txt','w')
# f.write(data)
# f.close()

# with open('theory.txt','r') as f:
#     data=f.read()
#     print(len(data))
#     print(f.tell())

# with open('theory.txt','w') as f:
    
#     print(f.tell())

# data1='''i am currently learning python'''
# with open('theory.txt','a+') as f:
#     f.write(data1)
#     f.seek(1)
#     print(f.write(data))

f=open('theory1.txt','x')
f.close()

    

    

