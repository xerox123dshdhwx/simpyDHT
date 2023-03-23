import random as rd

class Node:

    def __init__(self, env, id_simpy: int, id_node: int, entree_dht = None):
        self.connected = False
        self.entree_dht = entree_dht
        self.id_simpy = id_simpy
        self.id_node = id_node
        self.env = env
        self.right_neighbour = None
        self.left_neighbour = None
        self.action = env.process(self.run())

    def run(self):
        yield self.env.timeout(rd.randint(3, 20))
        if(self.connected) : 
            print("CONNECTION : ", self)
        print("TIME : ", self.env.now)
        while True:
            if(self.connected) :
                print(f'NODE {self.id_node} : connected and alive at {self.env.now}!')
                #yield self.env.timeout(rd.randint(15, 25))
            else : 
                yield self.env.timeout(rd.randint(3, 25))
                self.insert(self.entree_dht)


    def __str__(self):
        return f'Je suis le noeud simpy {self.id_simpy} , mon nom est {self.id_node} !      ({self.left_neighbour.id_node} <--> {self.right_neighbour.id_node})'

    def generator(self, duration):
        yield self.env.timeout(duration)

    # def verif(self):
    #     if(self.new_node.id_node > self.id_node and self.new_node.id_node < self.right_neighbour.id_node):
    #         self.insert()
    #     elif():
    #         pass

    def insert(self, entree_dht):
        if self.id_node > entree_dht.id_node and self.id_node < entree_dht.right_neighbour.id_node :
            self.right_neighbour = entree_dht.right_neighbour
            self.left_neighbour = entree_dht
            entree_dht.right_neighbour.left_neighbour = self
            entree_dht.right_neighbour = self
            self.connected = True
            print("CONNECTION : ", self)