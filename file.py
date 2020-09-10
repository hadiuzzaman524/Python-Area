file=open("jaman.txt")
count=0
for i in file:
    count+=1
print(count)


# for reading from file..........
with open('jaman.txt','r') as f:
    for i in f:
       if i.startswith("b"):
           print(i,end='')

# for writing into file....
with open('mantasha.txt','w') as mantasha:
    mantasha.write("my name is hadiuzzaman, and i love you so much")