class Node:

    def __init__(self, env, id_simpy: int, id_node: int,new_node = None):
        self.connected = False
        self.new_node = new_node
        self.id_simpy = id_simpy
        self.id_node = id_node
        self.env = env
        self.right_neighbour = None
        self.left_neighbour = None
        self.action = env.process(self.run())

    def run(self):
        print(self)
        while True:
            yield from self.generator(2)
            if(self.new_node != None):
                self.verif()


    def __str__(self):
        return f'Je suis le noeud simpy {self.id_simpy} , mon nom est {self.id_node} ! \n({self.left_neighbour.id_node} <--> {self.right_neighbour.id_node})'

    def generator(self, duration):
        yield self.env.timeout(duration)

    def verif(self):
        if(self.new_node.id_node > self.id_node and self.new_node.id_node < self.right_neighbour.id_node):
            self.insert()
        elif():
            pass

    def insert(self):
        pass
