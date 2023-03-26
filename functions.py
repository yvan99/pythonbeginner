def sumCalculator(firstNumber,secondNumber):
    sum = firstNumber + secondNumber
    return sum

print(sumCalculator(10,20)) # positional argument
print(sumCalculator( firstNumber= 10, secondNumber= 20)) #keyword argument

def emojiConverter(message):
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
    return output

emojiConverter(message = input("Enter a message"))


