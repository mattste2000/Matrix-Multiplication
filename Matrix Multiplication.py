#Remember to multiply N of a must equal M of b.  With result being Ma * Nb.
a = [[1,0,0,0],
    [0 ,1,0,0],
    [0 ,0,1,0],
    [0 ,0,0,1]]

b = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1],
    [12,13,14,15]]





#Resulting matrix !Need to edit dimensions in response to a & b
AB = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for m in range(len(a)):
    for n in range(len(b[0])):
       for R in range(len(b)):
           AB[m][n] += a[m][R] * b[R][n]
for r in AB:
   print(r)
