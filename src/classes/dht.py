import simpy
import random as rd
from src.classes.node import Node


class Dht:

    def __init__(self):
        self.env = simpy.Environment()
        self.array_node = []
        self.start()

    def start(self):

        n0 = Node(self.env, 0, 25)
        n1 = Node(self.env, 1, 2)
        n2 = Node(self.env, 2, 13)

        n0.right_neighbour = n1
        n0.left_neighbour = n2

        n1.right_neighbour = n2
        n1.left_neighbour = n0

        n2.right_neighbour = n0
        n2.left_neighbour = n1
        self.array_node.append(n0)
        self.array_node.append(n1)
        self.array_node.append(n2)

        for node in self.array_node:
            node.connected = True

        new_node = Node(env=self.env, id_simpy=3, id_node=6, entree_dht=n1)
        self.array_node.append(new_node)

        new_node = Node(env=self.env, id_simpy=4, id_node=18, entree_dht=n1)
        self.array_node.append(new_node)

        new_node = Node(env=self.env, id_simpy=5, id_node=29, entree_dht=n2)
        self.array_node.append(new_node)

        new_node = Node(env=self.env, id_simpy=6, id_node=3, entree_dht=n2)
        self.array_node.append(new_node)

        new_node = Node(env=self.env, id_simpy=7, id_node=28, entree_dht=n1)
        self.array_node.append(new_node)

        new_node = Node(env=self.env, id_simpy=8, id_node=1, entree_dht=n2)
        self.array_node.append(new_node)

        return self.array_node

    def get_random_connected_node(self):
        index = None
        node = None
        while node is None:
            index = rd.randint(0, len(self.array_node) - 1)
            if self.array_node[index].connected :
                node = self.array_node[index]
        return node
