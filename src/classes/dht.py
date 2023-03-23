import simpy
import random as rd
from classes.node import Node


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

        n0.right_neighbour = n1
        n0.left_neighbour = n2

        n1.right_neighbour = n2
        n1.left_neighbour = n0

        n2.right_neighbour = n0
        n2.left_neighbour = n1
        array.append(n0)
        array.append(n1)
        array.append(n2)

        for o in array :
            o.connected = True

        new_node = Node(env=self.env,id_simpy=3,id_node = rd.randint(2, 13), entree_dht=n1)

        #self.insert_node(n0, n1, n2)

        return array

    def insert_node(self, n0, n1, n2):
        new_node = Node(env=self.env,id_simpy=3,id_node = rd.randint(2, 13))
        if new_node.id_node > n1.id_node and new_node.id_node < n1.right_neighbour.id_node :
            new_node.right_neighbour = n1.right_neighbour
            new_node.left_neighbour = n1
            n1.right_neighbour.left_neighbour = new_node
            n1.right_neighbour = new_node
        # print(n1)
        # print(new_node)
        # print(n2)
        # print(n0)



