import re
import json
#fjerna tkinter
#import pygame as pg #lagt til pygame

print("Hello world")

answer=input('input your text (yes/no) :')

f = open('SPAMKEYWORDS.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

import json
import re

def load_spam_keywords(answer):
    with open("SPAMKEYWORDS.json", 'r') as f:
        spam_keywords = json.load(f)['spam_keywords']
    cleaned_keywords = [keyword.strip().lower() for keyword in spam_keywords]
    pattern = '|'.join(cleaned_keywords)
    pattern = re.compile(pattern, flags=re.IGNORECASE)
    return cleaned_keywords, pattern

#old
# def load_spam_keywords(answer):
#     with open("SPAMKEYWORDS.json", 'r') as f:
#         spam_keywords = json.load(f)['spam_keywords']
#     pattern = '|'.join(spam_keywords)
#     return spam_keywords, pattern

if answer.lower()=='yes':
    answer=input('check mail text :')
    print(answer)
spam_keywords, pattern = load_spam_keywords(answer)

if re.search(pattern, answer):
    print('Text contains SPAM keywords. Please Delete the mail you bitch and check the next one.')
    answer=input('do you want to close?(yes/no) :')
if answer.lower()=='yes':
    exit()
else:
    print('Text does not contain SPAM keywords.')
    print("close to restart")
    answer=input('do you want to close?(yes/no..) :')
    print(answer)
    print("fuck you")

if answer.lower()=='yes':
    exit()

while(True):
    pass
    

