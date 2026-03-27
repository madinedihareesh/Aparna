data=""
with open('python.jpeg','rb') as f:
    data=f.read()
    print(data)

with open('python1.jpeg','wb') as f:
    f.write(data)    