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
