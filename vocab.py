#!/usr/bin/python3
import json
from random import choice
#would uses choices(words,k=25) in 3.6

def getWords(n=25):
    with open('words/nouns.json', mode='r') as f:
        # At first, read the JSON file and store its content in an Python variable
        # By using json.load() function

        json_data = json.load(f)

        # So now json_data contains list of dictionaries
        # (because every JSON is a valid Python dictionary)
        words = json_data['data']
        selected=[ choice(words) for i in range(25)]
        return selected



 
