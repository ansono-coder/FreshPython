# the first program i need to fix during the rule pep8
my_food = ['pizza','falafel','carrot cake']
friend_foods = my_food[:]

for food in my_food:
    print(food)
for food in friend_foods:
    print(food)

# the second program i need to fix during the rule pep8
nums = []
for num in range(1,21,2):
    nums.append(num)

for num in nums:
    print(num)

# the third program i need to fix during the rule pep8
buffets = ('beef','mike','banana','nudoless','cake')

for buffet in buffets:
    print(buffet)

buffets[1] = 'blame'

