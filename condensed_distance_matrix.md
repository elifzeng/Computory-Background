[see also](https://stackoverflow.com/questions/13079563/how-does-condensed-distance-matrix-work-pdist)   
You can look at it this way: Suppose x is m by n. The possible pairs of m rows, chosen two at a time, is itertools.combinations(range(m), 2), e.g, for m=3:
```python
>>> import itertools
>>> list(combinations(range(3),2))
[(0, 1), (0, 2), (1, 2)]
```
So if d = pdist(x), the kth tuple in combinations(range(m), 2)) gives the indices of the rows of x associated with d[k].

Example:
```python
>>> x = array([[0,10],[10,10],[20,20]])
>>> pdist(x)
array([ 10.        ,  22.36067977,  14.14213562])
```
The first element is dist(x[0], x[1]), the second is dist(x[0], x[2]) and the third is dist(x[1], x[2]).

Or you can view it as the elements in the upper triangular part of the square distance matrix, strung together into a 1D array.

E.g.
```python
>>> squareform(pdist(x)) 
array([[  0.   ,  10.   ,  22.361],
       [ 10.   ,   0.   ,  14.142],
       [ 22.361,  14.142,   0.   ]])

>>> y = array([[0,10],[10,10],[20,20],[10,0]])
>>> squareform(pdist(y)) 
array([[  0.   ,  10.   ,  22.361,  14.142],
       [ 10.   ,   0.   ,  14.142,  10.   ],
       [ 22.361,  14.142,   0.   ,  22.361],
       [ 14.142,  10.   ,  22.361,   0.   ]])
>>> pdist(y)
array([ 10.   ,  22.361,  14.142,  14.142,  10.   ,  22.361])
```
