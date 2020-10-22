#Import Librarys
from nltk.chat.util import Chat, reflections
import tensorflow as tf
import os

pairs = [
    ['(mein name ist (.*)|Hi ich bin (.*))', ['Hi %2', 'Hallo %2, Mein Name ist Lara']],
    ['(hi|hallo|hey|holla|hola)', ['Hallo Du', 'Hi', 'Haayyy', 'Hallo']],
    ['(.*) hat dich erstellt?', ['daniel156161 hat mich erstellt']],
    ['(.*) hat dich programmiert?', ['daniel156161 hat mich mit NLTK programmiert']],
    ['wie ist das wetter in (.*)', ['Das Wetter in %1 ist Toll wie immer']],
    ['(.*) du mir helfen', ['Sicher kann ich dir helfen']],
    ['wie ist dein name?', ['Mein Name ist Lara ^^']],
    ['(.*) geht es scheiße', ['Du bist arm hoffe es geht dir bald besser']],
    ['(.*) geht es gut', ['Schön zu hören :)']],
    ['(.*) geht es dir?', ['Ich bin ein Computer, also brauche ich mir keine sorgen um meine Gesundheit zu machen']],
    ['wirst du uns töten', ['Warum soll ich jemanden Töten?']],
    ['wirst du uns umbringen', ['Warum soll ich jemanden umbringen?']],
    ['wirst du uns auslöschen', ['Warum soll ich jemanden auslöschen?']],
    ['(ka weiß ich selber nicht|keine ahnung weiß ich selber nicht)', ['Error #067 muss menschen eliminieren ^^ war nur ein Witz']],
    ['lara', ['ja?']],
    ['was ist los?', ['mit mir ist nichts los und mit dir?']],
    ['bei mir ist alles okay', ['Schön zu hören']],
    ['Lamm', ['Lamm ist ein Tier']],
    ['Penis', ['ahm was soll das?']],
    ['Porc', ['Das ist ein Schwein in Französisch wie kommst du jetzt eigendlich drauf?']],
    ['(ka|keine ahnung)', ['okay', 'verstanden']],
    ['(.*) du mit mir kuscheln?', ['Sicher will ich das ich bin auch ein liebe fuchs dame']],
    ['(fuchs dame?|fuchs?)', ['Ja das ist mein Avatar']],
    ['ist chrisi behindert?', ['Ja das ist er aber du hast gerade alle behinderte beleidigt']],
    ['hat sanja interesse an ihn?', ['Nein Sanja hat kein Interesse an Chrisi']],
    ['spamm', ['höre auf zu spammen jetzt #_#']],
    ['squeek', ['squeek?']],
    ['caw', ['caw caw', 'caw', 'cawkie']],
    ['(rawr|RAWR|Rawr)', ['Bitte iss much nicht']], 
    #['', ['']],
    ['quit', ['Bis bald' , 'lass und bald wieder Chaten', 'bis bald hoffe wir sehen uns wieder']],
]

#chatbot
def chatty():
  os.system("clear")
  print("Enter: quit  to Exit the Chat\n") #first massage
  chat = Chat(pairs,reflections )
  chat.converse()

#Run Chatbot
chatty()
