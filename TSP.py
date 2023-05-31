# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 9

def solve_tsp(G):
    visited = [0]
    source = 0

    while len(visited) < len(G):
        min_edge = min(i for i in G[source] if i != 0)
        node = G[source].index(min_edge)

        if node not in visited:
            visited.append(node)
            source = node
        else:
            G[source][node] = 0
    visited.append(0)
    return visited

