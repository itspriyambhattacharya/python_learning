myDict1 = {
    'first name': "Priyam",
    'last name': 'Bhattacharya',
    'age': 24
}

print(f"The dictionary is {myDict1}")

print(f"The first name is {myDict1['first name']}")

# changing values

myDict1['age'] = 25
print(f"The dictionary is {myDict1}")

# nested dictionary
print('================================================ Nested Dictionary ================================================')
tea_shop = {
    "tea1": {
        "masala": "spicy", "ginger": "zesty"
    },
    "tea2": {
        "green": "mild",
        "black": "strong"
    }
}

print(tea_shop)

print(tea_shop["tea1"])  # return a sub-dictionary
print(tea_shop["tea2"]["black"])
print(tea_shop.get("tea2"))
print(tea_shop.get("tea2").get("green"))
