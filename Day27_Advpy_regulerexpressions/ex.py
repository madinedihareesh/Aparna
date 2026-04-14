import re
'''
1.what is pattren ('abc',(ram)quantifier,[abc])
{8,16} 
1.it has to have aleast one cap aplha
2.lower aplha
3.numarics
4.spel(/!@#$%^&&**,.)
5.{altest 8 upto 16 chars} 

Welcome@123(11) '[\A\w\W\d]+{8,16}' (welcome)[welcome] 
Qwerty@123(10)
$Name$123456.  1234 4*3*2*1 24 26 0-9!@#$%^&*,./

function/methods:
match (it is going to verify wether the given pattren is at the staring 
of the string or not)
full match (is it exatly the same )
search (it is going with first occurence)
findall (prepare a list and how many times it is repeted in the
sting)
split (if we are spacifing a perticuler values it is going to split the string
with that pattren)
'''
# pattren='and' ##text
# s1='android'
# s2='handle'
# s3='and'

# print(re.match(pattren,s2))
# re.spli
# pat='very'
# s='Python is very easy to learn and very easy to code'
# print(re.search(pat,s))

# pat='Welcome@123'
# password='Welcome@123'
# print(re.fullmatch(pat,password).span())

# pat='can'
# s='can can a can is a canner'
# print(len(re.findall(pat,s))) ##text verfication pupose 

'''
john / jason
r filehangling
if 'john in listof:
     john.replace('jason)
'''

