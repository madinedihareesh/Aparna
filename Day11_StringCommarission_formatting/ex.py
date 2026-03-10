print(12>9)
print('banana'>'apple')
'''
Ascii values: (Amarican standed code for information interchange)
65-90: A-Z 97-122: a-z 0-9:48 to 57
chr()
ord()
'''
# print(chr(65))
# print(ord('A'))

# print(ord('b')>ord('a'))


# print('\u0042')

'Escape sequences:'
'''
\n:new line
'''
# print('Hi there!\nHow are you\ni am doing grate\ni hope you are doing fine')
# print('Hi hello\rT')
# print('Hi hello\f how are you')
# print('hi\thello')
# print('Hi\vhello')
# print('Hi thera\be')
# print('\ahi how are you')
# print('hi\\nhello')
# print('hi \\ hello')
# print('i am my father\'s son')
# print("yesterday i ahve seen a boy and he told that\"He lost\"")

# print('10\N{superscript two}')
# print('\N{yen sign}')
# print('\N{grinning face}')

# formatting string:

name='James'
age=25
sal=1.57
# print('My name is',name,'i am',age,'years old i am from',loc)

'''
%s=string
%i=intiger
%f=float
%F=float
%g=float
%d=decimal
%o=octal
%X=hexa decimal
'''
print('my name is %s i am %i years old and my sal is %g'%(name,age,sal))

print('my name is {} i am {} years old and my sal is {} lakhs'.format(name,age,sal))
print('my name is {} i am {} years old and my sal is {} lakhs'.format(sal,age,name))
print('my name is {2} i am {1} years old and my sal is {0} lakhs'.format(sal,age,name))

print(f'my name is {name} and i am {age} years old and my sal is {sal} lakhs')