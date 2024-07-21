friends = ['zelda','joke','minecraft']
print("Welcome to my house ! "+friends[0]+" have fun !")
print("Welcome to my house ! "+friends[1]+" have fun !")
print("Welcome to my house ! "+friends[2]+" have fun !")

print("We are so sorry to hear dear "+friends[1]+" will miss this party !")

friends[1] = "link"

print("Welcome to my house ! "+friends[0]+" have fun !")
print("Welcome to my house ! "+friends[1]+" have fun !")
print("Welcome to my house ! "+friends[2]+" have fun !")

print("----------------------------------")

print("ok,now we have a more large desk now !")

friends.insert(0,"mario")
friends.append("mars")

print("Welcome to my house ! "+friends[0]+" have fun !")
print("Welcome to my house ! "+friends[1]+" have fun !")
print("Welcome to my house ! "+friends[2]+" have fun !")
print("Welcome to my house ! "+friends[3]+" have fun !")
print("Welcome to my house ! "+friends[4]+" have fun !")

print("---------------------------------------------")

print("sorry ! i just have a small desk,so i just can welcome two friends now !")
del_friend_one = friends.pop()
print("sorry "+del_friend_one+" !")
del_friend_two = friends.pop()
print("sorry "+del_friend_two+" !")
del_friend_three = friends.pop()
print("sorry "+del_friend_three+" !")

print("Still welcome "+friends[0]+" !")
print("Still welcome "+friends[1]+" !")


del friends[0]
del friends[0]

print(friends)


