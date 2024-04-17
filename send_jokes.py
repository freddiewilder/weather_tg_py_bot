import functions as lib
from os import path

file = path.abspath('jokes.txt')
lib.send_jokes(file)

