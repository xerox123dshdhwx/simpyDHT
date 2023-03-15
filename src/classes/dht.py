import simpy
import random as rd
from src.classes.node import Node


class Dht:

    def __init__(self):
        self.env = simpy.Environment()
        self.array_node = self.create_ring()

    def connect(self):
        pass

    def create_ring(self):
        array = []
        n0 = Node(self.env, 0, 25)
        n1 = Node(self.env, 1, 2)
        n2 = Node(self.env, 2, 13)

        n0.right_neighbour = n2
        n0.left_neighbour = n1

        n1.right_neighbour = n2
        n1.left_neighbour = n0

        n2.right_neighbour = n1
        n2.left_neighbour = n0
        array.append(n0)
        array.append(n1)
        array.append(n2)

        return array

    def insert_node(self):
        new_node = Node(env=self.env,id_simpy=3,id_node = rd.randint(1,50))



