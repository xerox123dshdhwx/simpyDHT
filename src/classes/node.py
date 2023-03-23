import random as rd


class Node:

    def __init__(self, env, id_simpy: int, id_node: int, entree_dht=None):
        self.connected = False
        self.entree_dht = entree_dht
        self.id_simpy = id_simpy
        self.id_node = id_node
        self.env = env
        self.right_neighbour = None
        self.left_neighbour = None
        self.action = env.process(self.run())
        self.queue = []

    def run(self):
        yield self.env.timeout(rd.randint(3, 20))
        if (self.connected):
            print("CONNECTION : ", self)
        print("TIME : ", self.env.now)
        while True:
            if (self.connected):
                yield self.env.timeout(rd.randint(1, 5))
                if (len(self.queue) != 0):
                    print(self.queue)
                    if (self.queue[0][0] == "Connected"):
                        print("nouveau noeud ou regarder", self.queue[0][1].id_node)
                        print("moi", self.id_node)
                        self.insert(self, a_connecter=self.queue[0][1])
                    self.queue.pop(0)
                    print(self.queue)
            else:
                yield self.env.timeout(rd.randint(20, 25))
                print("rentre dans insert")
                self.insert(self.entree_dht)

    def __str__(self):
        return f'Je suis le noeud simpy {self.id_simpy} , mon nom est {self.id_node} !      ({self.left_neighbour.id_node} <--> {self.right_neighbour.id_node})'

    def generator(self, duration):
        yield self.env.timeout(duration)

    def verify(self, target, entree_dht):
        if target.id_node > entree_dht.id_node and target.id_node < entree_dht.right_neighbour.id_node:
            target.right_neighbour = entree_dht.right_neighbour
            target.left_neighbour = entree_dht
            entree_dht.right_neighbour.left_neighbour = target
            entree_dht.right_neighbour = target
            target.connected = True
            print("CONNECTION : ", target)
        else:
            print("on l'envoie a droite")
            print("ICIIIIIII", entree_dht.id_node)
            target.send_message("Connected", entree_dht.right_neighbour)

    def insert(self, entree_dht, a_connecter=None):
        if a_connecter == None:
            self.verify(self, entree_dht)
        else:
            self.verify(a_connecter, entree_dht)

    def send_message(self, message, right_neighbour):
        right_neighbour.queue.append([message, self])
        print(f"message envoyé à :{right_neighbour.id_node}")
