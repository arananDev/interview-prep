#https://structy.net/problems/undirected-path


def undirected_path(edges, node_A, node_B):
  graph = dict()
  for edge in edges:
    a,b = edge
    if a not in graph.keys(): graph[a] = []
    if b not in graph.keys(): graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)
  print(graph)
  
  stack = [node_A]
  checked = set()
  
  while len(stack) > 0: 
      current = stack.pop(-1)
      if current == node_B:
        return True
      [stack.append(item) for item in graph[current] if item not in checked]
      checked.add(current)
  return False


  ## biggest time complexity is e and space complexity is n