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
        if lo < hi:
            p = self.partition(A, lo, hi)
            self.quicksort(A, lo, p - 1)
            self.quicksort(A, p + 1, hi)

    def partition(self, A, lo, hi):
        """
            Lomuto partition with the last element as pivot.
            return: The final index of the pivot
        """
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
        # TODO: Bitte implementieren
        return A

if __name__ == "__main__":
    for s in [Bubblesort(), Quicksort(), Mergesort()]:
        a = [random.randint(0,100) for i in range(10)]
        # Test ob euer Sortierverfahren das gleiche zurueckgibt wie die Python Implementation
        assert s.sort(a) == sorted(a), \
                            "List is not propertly sorted. "+s.name+" returned: "+str(s.sort(a))+" but we expected: "+str(sorted(a))

    print "Well done! Now go and read: https://en.wikipedia.org/wiki/Timsort to see how Python does it."
