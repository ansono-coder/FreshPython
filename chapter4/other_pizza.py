pizzas = ['meat','fruit','banana','apple','orange']

friend_pizzas = list(pizzas)

print(pizzas)
print(friend_pizzas)

pizzas.append('cock')
print(pizzas)
print(friend_pizzas)

friend_pizzas.append('disk')
print(friend_pizzas)

print("my favorite pizzas are: "+str(pizzas)+" !")
print("my friend's pizzas are"+str(friend_pizzas)+" !")
