from collections import deque
class myQueue:
  def __init__(self):
    self.Q = deque()
  
  def deQueue(self):
    return self.Q.popleft()

  def enQueue(self, x):
    return self.Q.append(x)

  def isEmpty(self):
    return False if self.Q else True

def findConnectionLevel(n, Gmat, Px, Py):
  q = myQueue() 
  visited = [False for i in range(n)]
  q.enQueue(Px)
  q.enQueue(-1)
  visited[Px]=True
  level=1;

  while not q.isEmpty():
    v = q.deQueue()
    if (v == -1):
      level+=1
      if (not q.isEmpty()):
        q.enQueue(-1)
      continue
    for i in range(n):
      if(i==Py and Gmat[v][i] == 1):
        return level
      if(Gmat[v][i] and (not visited[i])):
        q.enQueue(i)
        visited[i]=True

  return 0

vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))