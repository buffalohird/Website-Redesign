
#calculates whether or not two graphs are isomorphic
#graphs are inputted as list of the nodes' connectivity
#included is the calculation for Module 12, Sample Problem 2
def determine_isomorphic(graph1, graph2):
  original1 = list(graph1)
  original2 = list(graph2)
  for x in original1:
    if x in graph2:
        graph1.remove(x)
        graph2.remove(x)
  if graph1 == [] and graph2 == []:
    print "%s is equal to %s" % (original1, original2)
    return True
  else:
    print "%s is not equal to %s" % (original1, original2)
    return False
    
#Module 12, Sample 2  
print "\nModule 12, Sample 2\n"
graphA = [2,2,2,2]
graphB = [2,2,2,2]
determine_isomorphic(graphA, graphB)

graphC = [2,2,3,2,3]
graphD = [1,4,2,2,2]
determine_isomorphic(graphC, graphD)

#Module 12, Homework 2
print "\nModule 12, Homework 2\n"
graph1 = [2,3,2,3,2,2]
graph2 = [2,2,3,2,3,2]
determine_isomorphic(graph1, graph2)


