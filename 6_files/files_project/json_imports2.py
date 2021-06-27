import json

file = open("friends_json.txt", "r")
file_contents = json.load(file)

file.close()

print(file_contents.items())



cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Toyota", "model": "Camry"}
]

file = open("cars_json.json", "w")
json.dump(cars, file)

file.close()