# While loop
is_learning =  True

while is_learning:
    print("You're learning")
    user_input = input("Are you still learning?: ")
    is_learning = user_input == "yes"


# Destructuring in for loop.
friends = [("Rolf", 25), ("Anne", 21), ("Charlie", 35)]
for name, age in friends:
    print(f"{name} is {age} years old.")


# Dictionary and for loops.
friends ={"Rolf": 25, "Anne": 21, "Charlie": 35}
for name in friends.values(): # to get just values of the dict.
    print(name)

friends ={"Rolf": 25, "Anne": 21, "Charlie": 35}
for name, age in friends.items(): # to get keys and values.
    print(f"{name} is {age} years old")


# Checking for prime numbbers.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} quals {x} * {n//x}")
            break
    else:
        print(f"{n} is prime numver.")


# List comprehension.
numbers = [1, 2, 3, 4, 5]
doubled_number = []
for  number in numbers:
    doubled_number.append(number * 2)
    print(doubled_number)
    
doubled_number = [number * 2 for number in range(2, 11)]
print(doubled_number)


# List comprehension to check a friend in the list with title casing.
friend = input("Enter your friend's name: ")
friends = ["Rolf", "Anne", "Ali", "Hoji"]
friends_lower = [name.lower() for name in friends]
if friend.lower() in friends_lower:
    print(f"Your friend {friend.title()} is here.")


# if statement in list comprehensions.
friends = ["rolf", "Anne", "Ali", "Hoji", "charlie"]
guests = ["Anne", "bob", "Ali", "james"]

friends_lower = [f.lower() for f in friends]
present_guests = [
    name.title()
    for name in guests
    if name.lower() in friends_lower
]
print(present_guests)


# Dictionary Comprehensions.
friends = ["Anne", "Ali", "Hoji", "Yahya"]
last_seen = [2, 5, 15, 8]
long_timers = {
    friends[i]: last_seen[i]
    for i in range(len(friends))
    if last_seen[i] > 5
}
print(long_timers)


# zip function to create dictionary and lists from two lists.
friends = ["Anne", "Ali", "Hoji", "Yahya"]
last_seen = [2, 5, 15, 8]

dict_version = dict(zip(friends, last_seen)) # Turns to a dictionary.
dict_version = list(zip(friends, last_seen)) # Turns to a zipped lists.
print(dict_version)


# The enumerate function in python.
friends = ["Anne", "Ali", "Hoji", "Yahya"]
counter = 0
for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

# better enumerate version
friends = ["Anne", "Ali", "Hoji", "Yahya"]
for friend, counter in enumerate(friends):
    print(counter)
    print(friend)

friends = ["Anne", "Ali", "Hoji", "Yahya"]
list_of_friends = list(enumerate(friends)) # Turning to enumerated list.
print(list_of_friends)

dict_of_friends = dict(enumerate(friends)) # Turning to enumerated dictionary.
print(dict_of_friends)

