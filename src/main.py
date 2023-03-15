import simpy
from classes.node import Node
import random as rd
from classes.dht import Dht


dht = Dht()
env = dht.env
env.run()

