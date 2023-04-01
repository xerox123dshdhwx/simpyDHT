from src.classes.dht import Dht


dht = Dht()
env = dht.env
print("\nDébut de simulation\n")
env.run(until=1000)
print("\nFin de simulation\n")

for i in dht.array_node:
    print(i)
