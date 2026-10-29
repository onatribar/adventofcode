import aoc_lube
import networkx as nx
from functools import cache

RAW = aoc_lube.fetch(year=2025, day=11)

def parse_raw():
    graph = nx.DiGraph()
    for line in RAW.strip().splitlines():
        src, rest = line.split(":")
        for dest in rest.split(): # hehe that rhymes
            graph.add_edge(src, dest)
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("Not a DAG!")
    return graph

DATA = parse_raw()

@cache
def n_paths(src, dest):
    if src == dest: return 1
    return sum(n_paths(next_node, dest) for next_node in DATA.successors(src))

def part_one():
    return n_paths("you", "out")
    
def part_two():
    a, b = "dac", "fft"
    return (n_paths("svr", a) * n_paths(a, b) * n_paths(b, "out")
        + n_paths("svr", b) * n_paths(b, a) * n_paths(a, "out"))

aoc_lube.submit(year=2025, day=11, part=1, solution=part_one)
aoc_lube.submit(year=2025, day=11, part=2, solution=part_two)