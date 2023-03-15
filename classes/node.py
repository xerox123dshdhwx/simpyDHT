class Node:

    def __init__(self, env, id_simpy: int, id_node: int):
        self.connected = False
        self.id_simpy = id_simpy
        self.id_node = id_node
        self.env = env
        self.right_neighbour = None
        self.left_neighbour = None
        self.action = env.process(self.run())

    def run(self):
        print(self)
        yield from self.generator(1)
        print(self.env.now)

    def __str__(self):
        return f'Je suis le noeud simpy {self.id_simpy} , mon nom est {self.id_node} !'

    def generator(self, duration):
        yield self.env.timeout(duration)


