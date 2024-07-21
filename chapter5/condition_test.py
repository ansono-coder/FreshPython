# the frist conditional test
book_name = 'red red rose'
print("the name of the book is red red rose ? i think yes")
print(book_name == 'red red rose')
print("the name of the book is dongking monkey ? i think it is not right")
print(book_name == 'dongking monkey')

# the second conditional test 
fav_num = 20
print("the fav_num is 34 ? i do not think it is right ")
print(fav_num == 34)
print("the fav_num is 20 ? i think it is right")
print(fav_num == 20)

# check string value 
name = 'jack'
name_other = 'Jack'
print(name == name_other) # false 

print(name.lower() == name_other.lower())

print(name.lower()+"\t"+name_other.lower())

# check nums
num_one = 12
num_two = 14
num_three = 12
print(num_one == num_two) # false
print(num_one == num_three) # true
print(num_two == num_three) # false
print(num_one != num_two) # true
print(num_two > num_one) #true
print(num_three < num_two) # true
print(num_one <= 12) # true
print(num_two >= 14) # true

# the use of and / or
user_names = ['jake','zelda','link','mario']
data_names = ['zelda','link','mario']
for usr in user_names:
    if(usr in data_names):
        print("Welcome my friend !"+usr.title())
    elif(usr not in data_names):
        print("Sorry you are not our custom !"+usr.title())
