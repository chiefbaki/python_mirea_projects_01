from car import *
from passengercar import *
from truck import *
import pickle


p1 = open('pickk', 'rb')
bmw = pickle.load(p1)
mers = pickle.load(p1)
print(bmw)
print(mers)

p2 = open('pickk', 'rb')
volvo = pickle.load(p2)
ford = pickle.load(p2)
daf = pickle.load(p2)
print(volvo)
print(ford)
print(daf)
