import networkx as nx

def day12_2(data):
    G = nx.Graph()
    for line in data.splitlines():
        G.add_edge(*line.split('-'))
    return sum(1 for _ in find_paths(G, double_visit=True))

def day12_1(data):
    G = nx.Graph()
    for line in data.splitlines():
        G.add_edge(*line.split('-'))
    return sum(1 for _ in find_paths(G))

def find_paths(G, current_path=['start'], double_visit=False):
    current_node = current_path[-1]
    for node in G.neighbors(current_node):
        new_path = current_path + [node]
        if node == 'end':
            yield new_path
        elif node.isupper() or node not in current_path:
            yield from find_paths(G, new_path, double_visit)
        elif double_visit and node != 'start':
            yield from find_paths(G, new_path, False)


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    data = fichier.read()
    print(day12_1(data))
    print(day12_2(data))