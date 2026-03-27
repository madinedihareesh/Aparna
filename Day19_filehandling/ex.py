# filehandling
# open(name of the file,'oparations')
'''
read r
writing w
appending a
x creation of new file
r+ read and write
w+ write and read
a+ append and read
rb read the binary data
wb write the binary data
'''
# f=open('data.txt','r')
# # print(f.readlines())
# print(f.readable())
# for i in f.readlines():
#     if 'have' in i:
#         print(i)

# f.close()
'''
for seek method
0: is representing satring of the file
1: is represting current postition of the file
2: is represting the ending postion of the file
'''
# para='\npython is very easy to learn'
# f=open('data1.txt','r+')
# f.read()
# f.write(para)
# f.close()
# str1='\ni am currently persuing python'
# f=open('data1.txt','a')
# f.write(str1)
# f.close()

# f=open('data3.txt','x')
# f.close()

# para='hi there how are you doing'
# f=open('data3.txt','w')
# f.write(para)
# print(f.writable())
# f.close()