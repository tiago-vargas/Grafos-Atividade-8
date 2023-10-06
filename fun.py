def compute_adjacency_list_from(adjacency_matrix: list[list[int]], node_names: list[str]) -> dict[str, list[str]]:
	result: dict[str, list[str]] = {}

	z = zip(node_names, adjacency_matrix)

	for (node_name, row) in z:
		neighbors: list[str] = []

		zz = zip(node_names, row)
		for (neighbor_name, element) in zz:
			if element == 1:
				neighbors.append(neighbor_name)

		result[node_name] = neighbors

	return result


def list_reacheable_nodes(adjacency_matrix: list[list[int]], node_names: list[str]) -> dict[str, list[str]]:
	neighbors = compute_adjacency_list_from(adjacency_matrix, node_names)
	result = {name: [] for name in node_names}
	for node in node_names:
		origin_node = node
		visited = set()
		reached_nodes = [origin_node]
		while reached_nodes != []:
			current_node = reached_nodes.pop()
			if current_node not in visited:
				visited.add(current_node)
				result[origin_node].append(current_node)
				reached_nodes += neighbors[current_node]

	for node in result:
		result[node] = [x for x in node_names if node in result]
		result[node] = [x for x in result[node] if x != node]

	return result

def count_connected_components(graph):
    visited = set()
    components = 0

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
            components += 1

    return components

def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        sorted_nodes.append(node)

    visited = set()
    sorted_nodes = []

    for node in graph.keys():
        if node not in visited:
            dfs(node)

    return list(reversed(sorted_nodes))

def partial_topological_sort(graph):
    in_degree = {} 
    for node in graph:
        in_degree[node] = 0

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = [node for node in graph if in_degree[node] == 0]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result