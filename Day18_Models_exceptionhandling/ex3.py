'''
Error:
try:
   rick code
except:
   error messages we ganarate for which type of error
else:
   any exception in not occored then this block code 
   should
finally:
   either it is trowning an exception or not it has to work
'''

try:
    age=int(input('enter the age'))
    res=age/0
except Exception as m:
    print(m)
else:
    print(age)
finally:
    print('program completed')             
      