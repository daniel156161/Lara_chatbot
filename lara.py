import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

import os

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('AI/words.pkl', 'rb'))
classes = pickle.load(open('AI/classes.pkl', 'rb'))
model = load_model('AI/Lara.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            restag = tag
            result = random.choice(i['responses'])
            break
    return result,restag

os.system('clear')
print("GO! Bot is running!")
print("")

while True:
    message = input("Input:  ")
    ints = predict_class(message)
    res = get_response(ints, intents)
#Emotes
    if res[1] == 'angry':
        emotion = '(ノ•̀ o •́ )ノ'
    elif res[1] == 'sad' or res[1] == 'noanswer':
        emotion = '｡ﾟ･（>﹏<）･ﾟ｡'
    elif res[1] == 'embarrassed' or res[1] == 'pet':
        emotion = '(◍•ᴗ•◍)❤️'
    elif res[1] == 'evil':
        emotion = '( •̀ᴗ•́ )و ̑̑'
    else:
        emotion = '⸜₍๑•⌔•๑ ₎⸝'
#Output
    if res[0] == "":
        print("Output:", emotion)
    else:
        print("Output:", res[0], emotion)
    print("")
    if res[1] == 'goodbye':
        break