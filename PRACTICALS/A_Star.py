import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue to hold nodes to explore
    open_set = []
    heapq.heappush(open_set, (0, start))

    # Store the shortest path cost from start to each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Store the parent of each node to reconstruct the path
    came_from = {}

    while open_set:
        # Get the node with the lowest f_score
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse the path

        for neighbor, cost in graph[current].items():
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                # Update g_score and parent
                g_score[neighbor] = tentative_g_score
                came_from[neighbor] = current
                # Add neighbor to open_set with its f_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # Return None if no path is found

# Define a simple graph
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 2},
    'D': {'G': 2},
    'E': {'G': 1},
    'F': {'G': 5},
    'G': {}
}

# Define heuristic values for each node (straight-line distance to the goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 3,
    'G': 0
}

# Run the A* algorithm
start_node = 'A'
goal_node = 'G'
path = a_star(graph, start_node, goal_node, heuristic)

# Print the result
if path:
    print(f"Shortest path from {start_node} to {goal_node}: {path}")
else:
    print("No path found.")