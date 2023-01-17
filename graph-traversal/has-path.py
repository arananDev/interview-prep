#https://structy.net/problems/has-path

def has_path(graph, src, dst):
  stack = [src]
  while len(stack) > 0: 
      current = stack.pop(-1)
      if current == dst:
        return True
      [stack.append(item) for item in graph[current]]
  return False

