#!/usr/bin/env python3
import skilstak.colors as c
import names

# Format for dictionaries
# player# = {
#   "name": "John Smith",
#   "plane": "The Eleventh",
#   "time": 0,
#   "distance": 0
# }


def welcome():
    print(c.clear, end='')
    print(c.green + '''Welcome to the Paper Airplane Competition System!
Just follow the easy directions to get started.''')

def infocollect():
    for count in range(len(names.names)):
        for name in names.names:
        

