# https://structy.net/problems/largest-component
def largest_component(graph):
  checked = set()
  best = 0
  
  for key in graph.keys():
    if key in checked:
      continue
    
    stack = [key]
    size = 0
    current_component = set()
    
    while len(stack) > 0:
      current = stack.pop(-1)
      [stack.append(item) for item in graph[current] if item not in checked]
      checked.add(current)
      current_component.add(current)
      
    size = len(current_component)
    if size > best: best = size
  
  return best
