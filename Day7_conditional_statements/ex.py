'''
if: it is basically for single desicion
'''
'''
amount=int(input('Enter the amount'))
if amount>0:
    print('It is a block if the amount is grater than 0')
'''

'''
if condition:
    blcok of code
else:
    block of code    
    
''' 

'''
ticket=False

if ticket:
    print('OK, you can watch the movie')
else:
    print('NO, you can not enter into the theather')    
'''
'''
num=int(input('Enter a number'))
if num%2==0:
    print('Even number')
else:
    print('ODD number')  
'''
'''
age=18
if age>=18:
    print('Major')
else:
    print('Minor')  

'''
# grade finder
'''
marks=65
if marks>0:
    if marks>=40 and marks<50:
        print('pass grade "D"')

    elif marks>=50 and marks<60:
        print('Grade "C"')
    elif marks>=60 and marks<70:
        print('Grade "B"')
    elif marks>70 and marks<=100:
        print('Grade "A"')
    else:
        print('Fail')              
'''
'''
bill=int(input('Enter the bill amount:'))
if bill>0:
    dis=0
    if bill>=5000:
        dis=bill*0.25
        totalbill=bill-dis
        print(totalbill)  
    elif bill>=3000 and bill<5000:
        dis=bill*0.15
        totalbill=bill-dis 
        print(totalbill)
    elif bill>=2000 and bill<3000:
        dis=bill*0.1
        totalbill=bill-dis 
        print(totalbill)
    else:
        print('No discount') 
'''
'''
age=16
res='Major' if age>18 else 'Minor'  
print(res) 
'''  
''' 
day=int(input('Enter the day number'))

match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuseday')
    case 3:
        print('Weds')
    case 4:
        print('Thurs')
    case 5:
        print('Friday')
    case 6:
        print('Sat')
    case _:
        print('Enter with in the range 1-6') 
'''

flavor=input('Enter the flavor of ice cream')

match flavor:
    case 'blackcurrent':
        print('It is available')
    case 'blackforect':
        print('It is available')
    case 'choco':
        print('It is available')
    case _:
        print('Sorry,we don\'t have that falvoe can you go with venila')            