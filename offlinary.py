from difflib import get_close_matches
import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.isupper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        yn=input("Did you mean %s instead? Enter Y if yes, and N if no: " % get_close_matches(word, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="N":
            return "The word you entered does not exist, please check again!!"            
        else:
            return "Invalid Selection!!"
    else:
        return "The word you entered doesn't exist, check again!!"

word = input("Please a word to know it's meaning: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item) #you can add {get_close_matches(word, data.keys())[0]+" is "+} in the print function!!
else:
    print(output)