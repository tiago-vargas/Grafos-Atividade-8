from fun import *


class TestComputingAdjacencyList:
	class TestUndirectedGraph:
		def test_small_adjacency_matrix(self):
			node_names = ['1', '2', '3', '4', '5']
			adjacency_matrix = [
				# 1, 2, 3, 4, 5
				[ 0, 1, 1, 0, 0],  # 1
				[ 1, 0, 1, 0, 0],  # 2
				[ 1, 1, 0, 1, 1],  # 3
				[ 0, 0, 1, 0, 0],  # 4
				[ 0, 0, 1, 0, 0],  # 5
			]

			l = compute_adjacency_list_from(adjacency_matrix, node_names)

			assert l == {
				'1': ['2', '3'],
				'2': ['1', '3'],
				'3': ['1', '2', '4', '5'],
				'4': ['3'],
				'5': ['3'],
			}

		def test_big_adjacency_matrix(self):
			node_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
			adjacency_matrix = [
				# 1, 2, 3, 4, 5, 6, 7, 8, 9
				[ 0, 1, 0, 1, 1, 0, 0, 0, 0],  # 1
				[ 1, 0, 1, 0, 1, 0, 0, 0, 0],  # 2
				[ 0, 1, 0, 0, 0, 0, 0, 0, 1],  # 3
				[ 1, 0, 0, 0, 1, 0, 0, 0, 0],  # 4
				[ 1, 1, 0, 1, 0, 0, 0, 0, 0],  # 5
				[ 0, 0, 0, 0, 0, 0, 1, 1, 0],  # 6
				[ 0, 0, 0, 0, 0, 1, 0, 1, 0],  # 7
				[ 0, 0, 0, 0, 0, 1, 1, 0, 0],  # 8
				[ 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 9
			]

			l = compute_adjacency_list_from(adjacency_matrix, node_names)

			assert l == {
				'1': ['2', '4', '5'],
				'2': ['1', '3', '5'],
				'3': ['2', '9'],
				'4': ['1', '5'],
				'5': ['1', '2', '4'],
				'6': ['7', '8'],
				'7': ['6', '8'],
				'8': ['6', '7'],
				'9': ['3'],
			}

	class TestDirectedGraph:
		def test_adjacency_matrix(self):
			node_names = ['1', '2', '3', '4', '5', '6']
			adjacency_matrix = [
				#  1,  2,  3,  4,  5,  6
				[  0,  0,  0, -1,  0,  0],  # 1
				[  0,  0, -1, -1,  0,  0],  # 2
				[  0,  1,  0, -1,  0,  0],  # 3
				[  1,  1,  1,  0, -1, -1],  # 4
				[  0,  0,  0,  1,  0,  1],  # 5
				[  0,  0,  0,  1, -1,  0],  # 6
			]

			l = compute_adjacency_list_from(adjacency_matrix, node_names)

			assert l == {
				'1': [],
				'2': [],
				'3': ['2'],
				'4': ['1', '2', '3'],
				'5': ['4', '6'],
				'6': ['4'],
			}


class TestCheckingConectivity:
	def test_checking_connected_graph(self):
		node_names = ['6', '7', '8']
		adjacency_matrix = [
			# 6, 7, 8
			[ 0, 1, 1],  # 6
			[ 1, 0, 1],  # 7
			[ 1, 1, 0],  # 8
		]

		result = is_strongly_connected(adjacency_matrix, node_names)

		assert result is True

	def test_checking_disconnected_graph(self):
		node_names = ['A', 'B', 'C']
		adjacency_matrix = [
			# A, B, C
			[ 0, 0, 1],  # A
			[ 0, 0, 0],  # B
			[ 1, 0, 0],  # C
		]

		result = is_strongly_connected(adjacency_matrix, node_names)

		assert result is False

	def test_connected_graph_with_no_immediate_neighbors(self):
		node_names = ['A', 'X', 'C']
		adjacency_matrix = [
			# A, X, C
			[ 0, 1, 0],  # A
			[ 1, 0, 1],  # X
			[ 0, 1, 0],  # C
		]

		result = is_strongly_connected(adjacency_matrix, node_names)

		assert result is True


class TestCheckingReacheability:
	def test_V_graph(self):
		"""
		```
		A     C
		 \\   /
		   X
		```
		"""
		node_names = ['A', 'X', 'C']
		adjacency_matrix = [
			# A, X, C
			[ 0, 1, 0],  # A
			[ 1, 0, 1],  # X
			[ 0, 1, 0],  # C
		]

		# neighbors = {
		# 	'A': ['X'],
		# 	'X': ['A', 'C'],
		# 	'C': ['X'],
		# }

		result = list_reacheable_nodes(adjacency_matrix, node_names)

		assert result == {
			'A': ['X', 'C'],
			'X': ['A', 'C'],
			'C': ['A', 'X'],
		}

	def test_T_graph(self):
		"""
		```
		A — X — C
		    |
		    D
		    |
		    E
		```
		"""
		node_names = ['A', 'X', 'C', 'D', 'E']
		adjacency_matrix = [
			# A, X, C, D, E
			[ 0, 1, 0, 0, 0],  # A
			[ 1, 0, 1, 1, 0],  # X
			[ 0, 1, 0, 0, 0],  # C
			[ 0, 1, 0, 0, 1],  # D
			[ 0, 0, 0, 1, 0],  # E
		]

		# neighbors = {
		# 	'A': ['X'],
		# 	'X': ['A', 'C', 'D'],
		# 	'C': ['X'],
		# 	'D': ['X', 'E'],
		# 	'E': ['D'],
		# }

		result = list_reacheable_nodes(adjacency_matrix, node_names)

		assert result == {
			'A': ['X', 'C', 'D', 'E'],
			'X': ['A', 'C', 'D', 'E'],
			'C': ['A', 'X', 'D', 'E'],
			'D': ['A', 'X', 'C', 'E'],
			'E': ['A', 'X', 'C', 'D'],
		}
