'''
Module os
os: 
'''
import os
import time

print(os.name) ##to find the name of the os
print(os.getcwd()) ##to find the currnt working Directory

os.chdir('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re/')
print(os.getcwd())

# with open('text.txt','x') as f:
#     pass
print(os.path.exists('/Users/pjangala/Desktop'))## to find wether the path is in existence or not
print(os.path.relpath('/Users/pjangala/Desktop/Aparna/'))
print(os.path.abspath('.'))
print(os.path.split('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re/ex1.py'))
print(os.path.join('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re', 'ex1.py'))
print(os.path.basename('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re/ex1.py'))
print(os.path.dirname('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re/ex1.py'))
print(os.listdir('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re'))
print(os.path.exists('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re/ex1.py'))
# t=os.path.getctime('/Users/pjangala/Desktop/Aparna/Day29_Advpy_re/ex1.py')
# print(time.ctime(t))
os.chdir('/Users/pjangala/Desktop/')
print(os.getcwd())
# os.mkdir('smaple1')
# # os.makedirs('grand/parent/child')
# os.removedirs('/grand/parent')
os.rmdir('sample1')
