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
