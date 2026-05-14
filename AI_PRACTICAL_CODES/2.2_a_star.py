import heapq

# A* Search Algorithm
def a_star(graph, start, goal, heuristic):

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    parent = {}

    while open_list:

        current_f, current_node = heapq.heappop(open_list)

        # Goal Node Reached
        if current_node == goal:

            path = []

            while current_node in parent:
                path.append(current_node)
                current_node = parent[current_node]

            path.append(start)
            path.reverse()

            return path, g_cost[goal]

        # Exploring Neighbor Nodes
        for neighbor, cost in graph[current_node].items():

            tentative_g_cost = g_cost[current_node] + cost

            if tentative_g_cost < g_cost[neighbor]:

                parent[neighbor] = current_node
                g_cost[neighbor] = tentative_g_cost

                f_cost = tentative_g_cost + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))

    return None, float('inf')


# ---------------- User Input Section ----------------

graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

# Taking graph input
for i in range(n):

    node = input("\nEnter node name: ")

    neighbors = {}

    m = int(input(f"Enter number of neighbors for {node}: "))

    for j in range(m):

        neighbor = input("Enter neighbor node: ")
        cost = int(input(f"Enter cost from {node} to {neighbor}: "))

        neighbors[neighbor] = cost

    graph[node] = neighbors

# Taking heuristic values
print("\nEnter Heuristic Values:")

for node in graph:
    heuristic[node] = int(input(f"h({node}) = "))

# Start and Goal Node
start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

# Printing Graph
print("\nGiven Graph:")

for node in graph:
    print(node, "->", graph[node])

# Calling A* Algorithm
path, cost = a_star(graph, start, goal, heuristic)

# Output
if path:
    print("\nShortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")
    
   
   
   #--------------------------------------------------------
    """
Sample Input

Enter number of nodes: 3

Enter node name: A
Enter number of neighbors for A: 1
Enter neighbor node: B
Enter cost from A to B: 1

Enter node name: B
Enter number of neighbors for B: 1
Enter neighbor node: C
Enter cost from B to C: 2

Enter node name: C
Enter number of neighbors for C: 0

Enter Heuristic Values:
h(A) = 3
h(B) = 1
h(C) = 0

Enter Start Node: A
Enter Goal Node: C


Expected Output

Shortest Path: A -> B -> C
Total Cost: 3
"""