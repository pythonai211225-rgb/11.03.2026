
a = [100]

grades = {
    #KEY  : VALUE
    2: 'a',
    "Dana": a,
    "Yossi": a,
    "Rina": [100, 90, 99],
    ("Dana", "Yossi", "Rina"): 99,
    (1,2): [1,2]  # work
}

# a[0] = 99
# b = (a,)
# print(b)
# a.append(20000)
# print(b)
# print(hash(print))
# print(hash('Dana'))
# print(hash('dana'))

emojis = {
    "happy": "😀",
    "sad": "😢",
    "fire": "🔥",
    "heart": "❤️"
}

print(emojis["heart"], emojis["happy"])
print(emojis.values())
print(emojis.keys())

coins = 'coins'
inventory = {
    'coins': 100,
    "lives": 3,
    "keys": 2
}

print(inventory[coins])

person = {
    "name": "Avi",
    "age": 20,
    "city": "Haifa"
}
person['age'] += 1
person['age'] = 21
print(person['age'])
#print(person.age)  # error

person['address'] = 'Tel Aviv'  # if not exist then create, if exist - override
print(person)

details = {}
details = dict()
details['age'] = 20  # creates new
print(details)
details['age'] = 21  # override
print(details)

print ("'age' in details?", 'age' in details)
print ("'age' in details?", 'age' in details.keys())
print ("20 in details?", 21 in details)
print ("20 in details.values()?", 21 in details.values())  # slow
print('age' in details and details['age'] == 21)
dict_age = details['age'] if 'age' in details else None
print(dict_age)
print(('age', 21) in details.items())

# create dictionary of yourself
# 'name', 'year_of_birth', 'address_city', 'height', 'phone', 'siblings' set/tuple/list

# BONUS: create dict of your addrres with: country, city, street
d = {
    'age': 18, # just example
    'address' : {

    }
}


