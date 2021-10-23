from os import popen


friends = input(
    "List three of your friend names, seprated by commas (no spaces, please): ").split(",")

people = open("people.txt", "r")
people_nearby = people.readlines()

people.close()

friends_set = set(people)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open("nearby_friends.txt", "w")
