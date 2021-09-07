# task 1
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x[1])
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print(students[0])
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z[0]['y'])

# task 2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan' },
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for name_dict in some_list:
        show_info = ""
        for the_key in name_dict.keys():
            show_info += f'{the_key} - {name_dict[the_key]}, '
        show_info = show_info[:len(show_info) - 2]
        print(show_info)
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel 

# task 3 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name, some_list):
    for name in some_list:
        print(name[key_name])
iterateDictionary2('first_name', students)


# task 4 
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printdojo(some_dict):
    for thing in some_dict.keys():
        print(len(some_dict[thing]))
        for nouns in some_dict[thing]:
            print(nouns)
printdojo(dojo)




