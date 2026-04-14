import re
'''
() set
[] group


auantifiers:
+ one or more
pat='[abc]+'
st='cccc'
print(re.fullmatch(pat,st).group())
* zero or more
? zero or one
{m} how many char the string has to have
{m,}has to be atleast m chars to any no of chars
{m,n}it has to be inbetween m to n
pat='[6-9]?[0-9]{9}' 
st='6234567890'
print(re.fullmatch(pat,st).group())

special char:
^[a-z] : if the cap is repsented infront of it.thenit should start with it
[^....]:if the cap is included at the starting of the group that means all the groued vales
represnted is excluded
. any char
$ it has be the ending of the string
r|s it has to be either r or s com|in|org
pat='^[a-z0-9!#$%^&*.]+@[a-z]+.(com|in)$'
st='hareesh.madinedi2024@gmail.com'
print(re.fullmatch(pat,st))

'''
