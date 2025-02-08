from collections import deque
class myStack:
  def __init__(self):
    self.stack = deque()
  
  def pop(self):
    return self.stack.pop()
  
  def push(self, x):
    return self.stack.append(x)

  def isEmpty(self):
    return False if self.stack else True

def runDFSForTankT(tanks, GList, t, visited):
  s = myStack()
  s.push(t)
  visited[t] = True

  while not s.isEmpty():
    i = s.pop()
    for p in GList[i]:
      if not visited[p]:
        s.push(p)
        visited[p] = True;

def findMasterTank(tanks, pipes):

  GList = {}
  for i in tanks:
    GList[i]=[]
  for (i,j) in pipes:
    GList[i].append(j)


  visited = {t:False for t in tanks}
  
  lastVisited = tanks[0] 

  for t in tanks:
    if not visited[t]:
      runDFSForTankT(tanks, GList, t, visited)
      lastVisited = t

  visited = {t:False for t in tanks}
  runDFSForTankT(tanks, GList, lastVisited, visited)

  for v in visited:
    if not visited[v]:
      return 0
  return lastVisited

v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))