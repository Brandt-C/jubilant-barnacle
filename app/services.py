#everything combined into models.  May consider using below for future implementation

# class Move:
#     def __init__(self, name):
#         self.name = name
#         result = r.get('https://pokeapi.co/api/v2/move/' + self.name)
#         data = result.json()
#         self.id = data['id']
#         self.power = data['power']
#         self.pp = data['pp']
        
#     def disp(self):
#         print(f"Name-{self.name}\tID-{self.id}\tPower-{self.power}\tPP-{self.pp}")
import time
from random import choices, sample

def choose4(arr):
    time.sleep(0.25)
    x = choices(arr, k=4)
    z = list(map(lambda x: str(x)[2:-3], x))
    return z

def funPhrase():
    x = [
        "thirsts for blood!",
        "is ready for battle.",
        "has been waiting all their life for this. . .",
        "drank lots of coffee this am and is ready to release some pent-up aggression!",
        "will destroy thine foes.",
        "- Please don't hurt me!",
        "thinks your team looks puny and can't wait to destroy them.",
        "will battle to the end of their hp.",
        "smells blood.",
        "will end you.",
        "is almost out of bubblegum."
    ]
    return sample(x,4)
