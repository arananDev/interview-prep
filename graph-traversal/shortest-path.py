def shortest_path(edges, node_A, node_B):
  graph = {}
  
  
  for edge in edges:
    a,b = edge 
    if a not in graph.keys(): graph[a] = []
    if b not in graph.keys(): graph[b] = []  
    
    graph[a].append(b)
    graph[b].append(a)
    
  print(graph)
  
  stack = [(node_A, 0)]
  checked = set()
  
  while len(stack) > 0:
    current, path_length = stack.pop(0)
    if current == node_B:
      return path_length
    [stack.append((node, path_length + 1)) for node in graph[current] if current not in checked]
    checked.add(current)
  
  return -1
