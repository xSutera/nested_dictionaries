x = [ [5,2,3], [10,8,9] ] 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
students[1]['last_name']='Bryant'
sports_directory['soccer'][0]='Andres'

z[0]['y']=30

def iterateDictionary(some_list):
    for x in some_list:
        print(x)

iterateDictionary(students)
print(' ')
def iterateDictionary2(key_name,some_list):
    for x in range(0,len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name',students)

def printInfo(some_dict):
    for x in some_dict:
        print(str(len(some_dict[x]))+" "+str(x))
        for y in range(0,len(some_dict[x])):
            print(some_dict[x][y])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)