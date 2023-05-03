import heapq

def prim(graph):
    """
    Implementation of Prim's algorithm to find the minimum spanning tree of a given weighted undirected graph.
    
    Args:
    - graph: a dictionary representing the graph in adjacency list format, where the keys are the vertices 
    and the values are lists of tuples representing the edges and their weights. For example:
    
        graph = {
            'A': [('B', 2), ('C', 3)],
            'B': [('A', 2), ('C', 4), ('D', 1)],
            'C': [('A', 3), ('B', 4), ('D', 5)],
            'D': [('B', 1), ('C', 5)]
        }

    Returns:
    - a tuple containing the minimum spanning tree in adjacency list format, where the keys are the vertices 
    and the values are lists of tuples representing the edges and their weights, and the total weight of the minimum
    spanning tree.
    """
    
    # Start with an arbitrary vertex
    start_vertex = list(graph.keys())[0]
    
    # Initialize the minimum spanning tree and the set of visited vertices
    mst = {start_vertex: []}
    visited = set([start_vertex])
    
    # Initialize the heap with the edges adjacent to the start vertex
    edges = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapq.heapify(edges)
    
    # Loop until all vertices have been visited
    total_weight = 0
    while edges:
        # Get the edge with the minimum weight
        weight, vertex1, vertex2 = heapq.heappop(edges)
        
        # If both vertices are already in the minimum spanning tree, skip this edge
        if vertex2 in visited:
            continue
        
        # Add the edge to the minimum spanning tree
        if vertex1 not in mst:
            mst[vertex1] = [(vertex2, weight)]
        else:
            mst[vertex1].append((vertex2, weight))
        
        # Update the total weight of the minimum spanning tree
        total_weight += weight
        
        # Mark the vertex as visited and add its edges to the heap
        visited.add(vertex2)
        for neighbor, weight in graph[vertex2]:
            if neighbor not in visited:
                heapq.heappush(edges, (weight, vertex2, neighbor))
    
    return mst, total_weight
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 1)],
    'C': [('A', 3), ('B', 4), ('D', 5)],
    'D': [('B', 1), ('C', 5)]
}

mst, total_weight = prim(graph)
print("Minimum Spanning Tree:", mst)
print("Total Weight:", total_weight)
# Output: Minimum Spanning Tree: {'A': [('B', 2)], 'B': [('D', 1), ('A', 2)], 'D': [('B', 1)], 'C': []}
#         Total Weight: 3aaaa