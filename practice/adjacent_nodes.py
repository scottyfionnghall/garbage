
# https://edabit.com/challenge/3DAkZHv2LZjgqWbvW

def get_nodes(matrix,nodes):
    node_pos1 = matrix[nodes[0]][nodes[1]]
    node_pos2 = matrix[nodes[1]][nodes[0]]
    if node_pos1 >= 1 and node_pos2 >= 1:
        print(True)
    else:
        print(False)

matrix = [
  [2,1,0,0,1,0],
  [1,0,1,0,1,0],
  [0,1,0,1,0,0],
  [0,0,1,0,1,1],
  [1,1,0,1,0,0],
  [0,0,0,1,0,0]
]

nodes = input('Enter nodes to compare:\n')
nodes = nodes.split(',')
nodes = [int(node) for node in nodes]
get_nodes(matrix,nodes)