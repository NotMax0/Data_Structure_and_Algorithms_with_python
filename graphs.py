class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = []
      self.gdict = gdict
# Get the keys of the dictionary
   def getVertices(self):
      return list(self.gdict.keys())
   def edges(self):
       return self.findedges()
       # Find the distinct list of edges
   def findedges(self):
       edgename = []
       for vrtx in self.gdict:
           for nxtvrtx in self.gdict[vrtx]:
               if {nxtvrtx, vrtx} not in edgename:
                   edgename.append({vrtx, nxtvrtx})
       return edgename
   def addVertex(self, vrtx):
       if vrtx not in self.gdict:
           self.gdict[vrtx] = []
       # Add the new edge
   def AddEdge(self, edge):
       edge = set(edge)
       (vrtx1, vrtx2) = tuple(edge)
       if vrtx1 in self.gdict:
           self.gdict[vrtx1].append(vrtx2)
       else:
           self.gdict[vrtx1] = [vrtx2]
# Create the dictionary with graph elements
graph_elements = {
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
g.addVertex("f")
print(g.getVertices())
print(g.edges())
# print(set((12, 13)))
# v1, v2 = tuple({12, 13})
# print(v1, v2)
g.AddEdge({'a','e'})
print(g.edges())