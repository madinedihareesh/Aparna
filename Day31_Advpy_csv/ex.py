import os
import csv
from pprint import pprint
print(os.getcwd())
os.chdir('/Users/pjangala/Desktop')
print(os.getcwd())

# empdetails=[]
# with open('emp.csv','r') as file:
#     reader=csv.reader(file)
#     next(reader)
#     for line in reader:
#         empdetails.append(line)
# print(empdetails)   

# empdetails=[]
# with open('emp.csv','r') as file:
#     reader=csv.DictReader(file)
#     for detail in reader:
#         empdetails.append(detail)
# print(empdetails)  
 
# empdetails={}
# with open('emp.csv','r') as file:
#     reader=csv.DictReader(file)
#     for detail in reader:
#         empdetails[detail['Name']]=detail
# # pprint(empdetails) 

# for i in empdetails:
#     if i == 'Divya':
#         if int(empdetails[i]['Sal'])>700000:
#             print(empdetails[i])
#             break
#         else:
#             print('The person name divya is not having sal above 700000') 
#     else:
#         print('There is no person named Divya')   
  
# with open('gro.csv','w') as file:
#     writer=csv.writer(file)
#     writer.writerow(['name','price','mfd','exd'])
#     for i in range(1,6):
#         name=input('Enter the name of the item: ')
#         price=input('Enter the Price of the item')
#         mfd=input('Enter mfd date: ')
#         exd=input('Enter exd date: ')
#         writer.writerow([name,price,mfd,exd])
fieldname=['name','price','warenty']
with open('items.csv','w',newline='') as file:
    
    writer=csv.DictWriter(file,fieldnames=fieldname)
    writer.writeheader()
    writer.writerow({'name':'fan','price':'2500','warenty':'3years'})
    writer.writerow({'name':'tv','price':'25000','warenty':'2years'})
    writer.writerow({'name':'light','price':'250','warenty':'1years'})
    writer.writerow({'name':'laptop','price':'170000','warenty':'NUll'})
    
          