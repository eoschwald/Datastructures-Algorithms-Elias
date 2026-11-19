import random

class Sorter:
    def sort(self, A):
        """
            Sort a list A in increasing order.
            Important: Always return a *copy* of the input list A, do *not* change the list A 
                       
            return: The sorted list A
        """
        raise NotImplementedError

class Bubblesort(Sorter):
    """
        Implements BUBBLESORT as discussed in the lecture
    """
    name = "BUBBLESORT"
    def sort(self, A):
        A = list(A)
        n = len(A)
        for i in range(n - 1):
            swapped = False
            # After pass i, the last i elements are already in their final position
            for j in range(n - 1 - i):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    swapped = True
            if not swapped:
                break
        return A


class Quicksort(Sorter):
    """
        Implements QUICKSORT as discussed in the lecture
    """
    name = "QUICKSORT"
    def sort(self, A):
        A = list(A)
        self.quicksort(A, 0, len(A) - 1)
        return A

    def quicksort(self, A, lo, hi):
        # Recurse into the smaller part and loop over the larger one,
        # so the recursion depth stays O(log n) even in the worst case
        while lo < hi:
            p = self.partition(A, lo, hi)
            if p - lo < hi - p:
                self.quicksort(A, lo, p - 1)
                lo = p + 1
            else:
                self.quicksort(A, p + 1, hi)
                hi = p - 1

    def partition(self, A, lo, hi):
        """
            Lomuto partition with a random pivot (moved to the last position).
            return: The final index of the pivot
        """
        r = random.randint(lo, hi)
        A[r], A[hi] = A[hi], A[r]
        pivot = A[hi]
        i = lo - 1
        for j in range(lo, hi):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[hi] = A[hi], A[i + 1]
        return i + 1

class Mergesort(Sorter):
    """
        Implements MERGESORT as discussed in the lecture
        Tipp: Moeglicherweise eine Hilfs-methode merge(self, links, rechts) implementieren
    """
    name = "MERGESORT"
    def sort(self, A):
        A = list(A)
        if len(A) <= 1:
            return A
        mid = len(A) // 2
        links = self.sort(A[:mid])
        rechts = self.sort(A[mid:])
        return self.merge(links, rechts)

    def merge(self, links, rechts):
        result = []
        i = j = 0
        while i < len(links) and j < len(rechts):
            if links[i] <= rechts[j]:
                result.append(links[i])
                i += 1
            else:
                result.append(rechts[j])
                j += 1
        result.extend(links[i:])
        result.extend(rechts[j:])
        return result

class Heapsort(Sorter):
    """
        Implements HEAPSORT as discussed in the lecture
    """
    name = "HEAPSORT"
    def sort(self, A):
        A = list(A)
        n = len(A)
        # Build a max-heap, starting at the last node that has children
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(A, i, n)
        # Move the current maximum to the end and restore the heap on the rest
        for end in range(n - 1, 0, -1):
            A[0], A[end] = A[end], A[0]
            self.sift_down(A, 0, end)
        return A

    def sift_down(self, A, i, n):
        """
            Sink A[i] until the subtree rooted at i is a max-heap.
            Only the first n elements of A belong to the heap.
        """
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and A[left] > A[largest]:
                largest = left
            if right < n and A[right] > A[largest]:
                largest = right
            if largest == i:
                return
            A[i], A[largest] = A[largest], A[i]
            i = largest

if __name__ == "__main__":
    for s in [Bubblesort(), Quicksort(), Mergesort(), Heapsort()]:
        a = [random.randint(0,100) for i in range(10)]
        # Test ob euer Sortierverfahren das gleiche zurueckgibt wie die Python Implementation
        assert s.sort(a) == sorted(a), \
                            "List is not properly sorted. "+s.name+" returned: "+str(s.sort(a))+" but we expected: "+str(sorted(a))

    print ("Well done! Now go and read: https://en.wikipedia.org/wiki/Timsort to see how Python does it.")
