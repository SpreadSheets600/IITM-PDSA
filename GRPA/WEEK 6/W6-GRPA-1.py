class min_heap:
    def __init__(self):
        self.size = 0
        # The below is a list of tuples. In every tuple one value
        # is the element from list and the second value identifies the list.
        self.arr = []

    def isempty(self):
        return True if (self.size == 0) else False

    # Heapify element at index i
    def heapify_down(self, i):
        n = self.size
        a = self.arr
        while i < n:
            ss = l = 2 * i + 1
            r = 2 * i + 2
            # ss is smaller of left and right child
            if l < n and r < n and a[l][0] > a[r][0]:
                ss = r
            if ss < n and a[ss][0] < a[i][0]:
                a[i], a[ss] = a[ss], a[i]
                i = ss
            else:
                break

    def delete_min(self):
        min = self.arr[0]
        last = self.arr.pop()
        # size of heap after pop operation will reduce by 1
        self.size -= 1
        if self.size > 0:
            self.arr[0] = last
            self.heapify_down(0)
        return min

    # Heapify last element in the heap
    def heapify_up(self):
        i = self.size - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.arr[i][0] < self.arr[parent][0]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break

    # Insert to min heap
    def insert_min_heap(self, x):
        self.arr.append(x)
        self.size += 1
        self.heapify_up()


def mergeKLists(L):
    k = len(L)
    h = min_heap()
    finalList = []

    # Insert first element from each k lists to heap.
    for i in range(k):
        tup = (L[i][0], i)
        h.insert_min_heap(tup)

    kPointers = [
        1 for i in range(k)
    ]  # As all 0th elements will be inseted into the heap of size k
    while not h.isempty():
        tup = h.delete_min()
        finalList.append(tup[0])
        listNumber = tup[1]
        if kPointers[listNumber] < len(L[listNumber]):
            tup = (L[listNumber][kPointers[listNumber]], listNumber)
            h.insert_min_heap(tup)
            kPointers[listNumber] += 1

    return finalList


k = int(input())
LL = []
for i in range(k):
    subL = [int(item) for item in input().split(" ")]
    LL.append(subL)
print(*mergeKLists(LL))
