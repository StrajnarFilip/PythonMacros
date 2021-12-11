from Actions import *

def Trees():
    print("I like trees")
def Plants():
    print("I like plants")

LogCoordinatesOnClick()

NewKeybind("<ctrl>+a",Trees)
NewKeybind("<ctrl>+b",Plants)

BlockThread()