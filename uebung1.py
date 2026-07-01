def subsets(A):
   result = [[]]
   for x in A:
       neue_teilmengen = []
       for teilmenge in result:
           neue_teilmengen.append(teilmenge + [x])
       result = result + neue_teilmengen
   return result

print(subsets([1, 2, 3]))