string1 = 'bangladesh is my motherland'
print(string1[5:]) # print 5th to last character
print(string1[:5]) # print 0th to 5th character
print(string1[:]) # print all character of the string
#concat the string...........
string2='amr '+string1[0:]
print(string2)
print('length of string',len(string1)) #find length of the string
print(string1.split()) # devide sentence into words
print(string1.find('is')) #return the index if found
if string1.startswith('h'): #return true if start with specific char
    print('true')
else:
    print('false')
if string1.endswith('d'): #return true if end with specific char
    print('true')
else:
    print('false')
if string1.islower(): #return true if sentence is lowercase
    print('lowercase')
else:
    print('uppercase')

if string1.isupper(): #return true if sentence is uppercase
    print('uppercase')
else:
    print('lowercase')

var='Bangladesh'
print(var.upper()) #convert uppercase
print(var.lower()) #convert lowercase

myinfo='Hadiuzzaman hadiuzzaman908@gmail.com 01785304677'
pos=myinfo.find('h')
print(pos)
des=myinfo.find(' ',pos) # return position ' ' after pos
print(des)
print('my email: ',myinfo[pos:des]) # return a substring between pos to des
