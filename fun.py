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
