from fun import *


class TestComputingAdjacencyList:
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

		assert l == [
			['2', '3'],
			['1', '3'],
			['1', '2', '4', '5'],
			['3'],
			['3'],
		]

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

		assert l == [
			['2', '4', '5'],
			['1', '3', '5'],
			['2', '9'],
			['1', '5'],
			['1', '2', '4'],
			['7', '8'],
			['6', '8'],
			['6', '7'],
			['3'],
		]
