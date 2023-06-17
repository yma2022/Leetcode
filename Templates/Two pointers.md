## Two pointers (same direction)

```
j = 1
for i from 0 to n - 1:
  while j < n and (i, j) != condition:
    j += 1
  if j >= n:
    break
  process (i, j)
```



## Two pointers (inverse direction)

```
i, j = 0, n - 1
while i < j:
  if condition:
    i += 1
  else:
    j -= 1
```
