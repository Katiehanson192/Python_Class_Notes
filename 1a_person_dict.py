person = {}
person['fname'] = 'Joe'
person['lname'] = 'Fonebone' 
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'} 

#print(person)

#print(type(person['children']))

#children is a list, so to print out Betty, use code below

print(person['children'][2])
#children = key, [2] = index in list

print(person['pets']['cat'])
#dealing w/ a dictionary w/i a dictionary, so need to use 2 KEYS
#gives name of cat 'sox'



for i in person['children']:
     print(i)
     #person['children'] = list, i = iterrator

for i,j in person['pets'].items():
     print(i)
     




                      
