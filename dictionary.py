# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# } ### keys should be unique, case sensitive
# print(customer['name']) #John Smith
# print(customer["gender"]) #KeyError
# print(customer.get("birthdate")) #None
# print(customer.get("gender", "Female")) #Female, add new key
# customer["name2"] = "Pascal" # add new key name2

####### EXERCISE #########
# phone = input("Phone: ")
# digits_mapping = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# output = ""
# for char in phone:
#     output += digits_mapping.get(char, "!") + " "
# print(output)

####### EMOJI CONVERTOR ###########

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😃",
        ':(': '😔',
        ':D': '😁',
        "<3": "❤",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter((message)))

