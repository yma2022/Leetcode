# Union Find / Disjoint Sets Note

## What is Union Finding?

Given the vertices and edges between them, how could we quickly check whether two vertices are connected? For example, Figure 5 shows the edges between vertices, so how can we efficiently check if 0 is connected to 3, 1 is connected to 5, or 7 is connected to 8? We can do so by using the “disjoint set” data structure, also known as the “union-find” data structure. Note that others might refer to it as an algorithm. In this Explore Card, the term “disjoint set” refers to a data structure.

## What is the trick?
- Quick find
  
	```
	#UnionFind class
	class UnionFind:
	    def __init__(self, size):
		self.parents = [i for i in range(size)]
	
	    def find(self, x):
		return self.root[x]
			
	    def union(self, x, y):
		parentX = self.find(x)
		parentY = self.find(y)
		if parentX != parentY:
		    for i in range(len(self.parents)):
			if self.parents[i] == parentY:
			    self.parents[i] = parentX
	
	    def isConnected(self, x, y):
		return self.find(x) == self.find(y)
	
	
	#Test Case
	uf = UnionFind(10)
	#1-2-5-6-7 3-8-9 4
	uf.union(1, 2)
	uf.union(2, 5)
	uf.union(5, 6)
	uf.union(6, 7)
	uf.union(3, 8)
	uf.union(8, 9)
	print(uf.connected(1, 5))  # true
	print(uf.connected(5, 7))  # true
	print(uf.connected(4, 9))  # false
	#1-2-5-6-7 3-8-9-4
	uf.union(9, 4)
	print(uf.connected(4, 9))  # true
	```
- Quick union
	  ```
	  #UnionFind class
	  class UnionFind:
	      def __init__(self, size):
	          self.root = [i for i in range(size)]
	  
	      def find(self, x):
	          while x != self.root[x]:
	              x = self.root[x]
	          return x
	  		
	      def union(self, x, y):
	          rootX = self.find(x)
	          rootY = self.find(y)
	          if rootX != rootY:
	              self.root[rootY] = rootX
	  
	      def connected(self, x, y):
	          return self.find(x) == self.find(y)
	  
	  
	  # Test Case
	  uf = UnionFind(10)
	  # 1-2-5-6-7 3-8-9 4
	  uf.union(1, 2)
	  uf.union(2, 5)
	  uf.union(5, 6)
	  uf.union(6, 7)
	  uf.union(3, 8)
	  uf.union(8, 9)
	  print(uf.connected(1, 5))  # true
	  print(uf.connected(5, 7))  # true
	  print(uf.connected(4, 9))  # false
	  # 1-2-5-6-7 3-8-9-4
	  uf.union(9, 4)
	  print(uf.connected(4, 9))  # true
	  ```
- Union by rank

  ```
  # UnionFind class
  class UnionFind:
      def __init__(self, size):
          self.root = [i for i in range(size)]
          self.rank = [1] * size
  
      def find(self, x):
          while x != self.root[x]:
              x = self.root[x]
          return x
  		
      def union(self, x, y):
          rootX = self.find(x)
          rootY = self.find(y)
          if rootX != rootY:
              if self.rank[rootX] > self.rank[rootY]:
                  self.root[rootY] = rootX
              elif self.rank[rootX] < self.rank[rootY]:
                  self.root[rootX] = rootY
              else:
                  self.root[rootY] = rootX
                  self.rank[rootX] += 1
  
      def connected(self, x, y):
          return self.find(x) == self.find(y)
  
  
  # Test Case
  uf = UnionFind(10)
  # 1-2-5-6-7 3-8-9 4
  uf.union(1, 2)
  uf.union(2, 5)
  uf.union(5, 6)
  uf.union(6, 7)
  uf.union(3, 8)
  uf.union(8, 9)
  print(uf.connected(1, 5))  # true
  print(uf.connected(5, 7))  # true
  print(uf.connected(4, 9))  # false
  # 1-2-5-6-7 3-8-9-4
  uf.union(9, 4)
  print(uf.connected(4, 9))  # true
  ```


### Template
