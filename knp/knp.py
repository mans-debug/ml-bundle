import networkx as nx
import matplotlib.pyplot as plt
import random as rnd

colors = [
    'brown',
    'maroon',
    'aaroon',
    'tan',
    'lime',
    'navy',
    'indigo',
    'violet',
    'purple',
    'blue',
    'green',
    'red',
    'cyan',
    'magenta',
    'yellow',
]


def draw_graph(G, node_color=None):
    if node_color is None:
        node_color = ['#1f78b4'] * len(G)
    pos = nx.spring_layout(G, seed=10)  # positions for all nodes - seed for reproducibility
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=node_color)
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=12)
    weight_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, weight_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def random_weight(graph):
    low_bound = 1
    high_bound = 100
    weighed_graph = nx.Graph()
    for a, b in graph.edges:
        wht = rnd.uniform(low_bound, high_bound)
        wht = round(wht, 1)
        weighed_graph.add_edge(a, b, weight=wht)
    return weighed_graph


def first_weight_adjacent(adjacency_dict):
    res = None
    for node, opt in adjacency_dict.items():
        res = node, opt['weight']
        break
    return res


def kruskal_algo(graph):
    nodes = graph.nodes
    mst = nx.Graph()
    graph.edges.items()
    sorted_edges = sorted(graph.edges.data(True), key=lambda x: x[2]['weight'])
    for a, b, weight in sorted_edges:
        weight = weight['weight']
        mst.add_edge(a, b, weight=weight)
        if next(nx.simple_cycles(mst), None) is not None:
            mst.remove_edge(a, b)
        if mst.nodes == nodes:
            break
    return mst


def main():
    vertices = 5
    graph = nx.complete_graph(vertices)
    weighed_graph = random_weight(graph)
    draw_graph(weighed_graph)


def remove_k_longest_edges(g, k):
    sorted_edges = sorted(g.edges.data(True), key=lambda x: x[2]['weight'], reverse=True)
    if k > len(sorted_edges):
        raise "Amount of clusters bigger then number of edges"
    for a, b, _ in sorted_edges:
        g.remove_edge(a, b)
        k -= 1
        if k == 0:
            break
    return g


def clusterize(g, k):
    shortened = remove_k_longest_edges(g, k)
    colormap = {}
    for component in nx.connected_components(shortened):
        color = colors.pop()
        for c in component:
            colormap[c] = color
    return shortened, [colormap[node] for node in shortened.nodes]


if __name__ == '__main__':
    graph = nx.complete_graph(20)
    graph = random_weight(graph)
    draw_graph(graph)
    min_spanning_tree = kruskal_algo(graph)
    draw_graph(min_spanning_tree)
    draw_graph(nx.minimum_spanning_tree(graph))
    k = 7
    clusterized, colormap = clusterize(min_spanning_tree, k)
    draw_graph(clusterized, colormap)
