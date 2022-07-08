from collections import defaultdict
from typing import List
from heapq import heapify, heappush, heappop


def prims_algo(edges: List[List[int]], weights: int) -> List[List[int]]:
    """
    1. Start from any vertex.
    2. Add neighbors of the selected vertex into a candidate list.
    3. From the candidate list, select an unvisted vertex with minimum cost.
    4. Repeat 2 and 3 until all vertices are selected. 

    Heap can be used to maintain a list of candidate edges.
    Since we always select vertex from unvisited vertices, there is no need to detect cycles.

    """
    adj_list = defaultdict(list)

    for [v1, v2], cost in zip(edges, weights):
        adj_list[v1].append((cost, v2, [v1, v2]))
        adj_list[v2].append((cost, v1, [v1, v2]))

    result: List[int] = []
    candidates: int = []
    visited = set()

    start_pt = edges[0][0]
    candidates.extend(adj_list[start_pt])
    visited.add(start_pt)
    heapify(candidates)

    while len(result) < len(adj_list) and len(candidates) > 0:

        _, selected_vertex, selected_edge = heappop(candidates)

        if selected_vertex in visited:
            continue

        visited.add(selected_vertex)
        result.append(selected_edge)

        for neighbor in adj_list[selected_vertex]:
            _, neighbor_vertex, _ = neighbor

            if neighbor_vertex not in candidates:
                heappush(candidates, neighbor)

    return result
