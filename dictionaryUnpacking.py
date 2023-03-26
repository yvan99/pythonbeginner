# unpacking in python
cordinates = [5,3,2] # also appied to tuples
x,y,z = cordinates
print(x,y,z)


customer = {
    "names":"John Doe", # each dictionary key should be unique
    "age":30,
    "address":"kigali st",
    "is_verified":True
}
print(customer.get("names"))
print(customer.get("birthdate","Jan first")) # if the key is not present , set default value
#update keys
customer["names"] = "Jane Doe"
# add key
customer["birthdate"] = "Jan 2nd"
print(customer.get("names"))

# dictionary emoji converter

message = input(">")
wordSplitter = message.split(" ")
emojis = {
    ":)":"😅",
    ":D":"😂",
    ":P":"😊",
    ":(": "😁",
    ":O":"😂",
    ":P":"😊",
    ":P":"😊",
    ":(":"😞" 
}
output = ""
for word in wordSplitter:
    emojis.get(word,word)
    output += emojis.get(word,word)
    print(output)