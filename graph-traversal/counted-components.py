#https://structy.net/problems/connected-components-count

def connected_components_count(graph):
  count = 0
  checked = set()
  
  for key in graph.keys():
    if key in checked:
      continue
    
    stack = [key]
    while len(stack) > 0:
      current = stack.pop(-1)
      [stack.append(item) for item in graph[current] if item not in checked]
      checked.add(current)
      
    count += 1
    
  
  return count