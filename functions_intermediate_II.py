# How would you change the value 10 in x to 15?  Once you're done x should then be[[5, 2, 3], [15, 8, 9]].

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?

# For the sports_directory, how would you change 'Messi' to 'Andres'?

# For z, how would you change the value 20 to 30?


# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# x [1][1] = 15

# print(x)

# students [0]['last_name'] = 'Bryant'

# print(students)

# sports_directory['soccer'][0] = 'Andres'

# print(sports_directory)

# z[0]['y'] = 30

# print(z)

# ------------------------------------------
# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:


# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# for name in range(len(students)):
#     print (students[name]['first_name'], students[name]['last_name'])

# or 

# for item in students:
#     print ("first_name - " + item['first_name'], "last_name - " + item['last_name']) 

# --------------------------

# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# for name in students:
#     print (name['first_name'])

# or 

# def fname():
#     for name in students:
#         print (name['first_name'])

# fname()


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


# print (dojo['locations'], dojo['instructors'])

# def places():
#     print("Locations")
#     for local in dojo['locations']:
#         print(local)
#         print("Instructors")
#         for teachers in dojo['instructors']:
#             print(teachers)

# places()
