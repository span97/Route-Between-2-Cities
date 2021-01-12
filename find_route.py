import sys
from queue import PriorityQueue

file = sys.argv[1]
start = sys.argv[2]
if(len(sys.argv)<4):
	print("Not Enough arguments")
else:
	goal = sys.argv[3]

# Function Uniform-cost-Search which return Solution or Failure
def UninformedSerch(graph,start,goal):
	#A priority Queue ordered by path cost 
	fringe=PriorityQueue()

	# An empty set to store the nodes explored
	nodesVisited=set()
	#a list to store the route and parentNodes, to construct the route

	route=[]
	parentNodes={}
	#Initilaize 

	nodesExpanded=0
	nodesGenerated=0
	PathCost=0
	
	"""
	When the the Origin City is the Destination City 

	"""
	if (start==goal):
		nodesExpanded +=1
		DestinationPath=start
		return 0 , nodesExpanded , nodesGenerated, PathCost 

	nodesGenerated+=1
	fringe.put((PathCost,start,None,0))	#Add elements into the fringe

	""" loop that keeps running until the fringe becomes empty """

	while not fringe.empty():

		PathCost,current,pNode,cost = fringe.get()

		nodesExpanded +=1 

		""" Check if the State is explored or not, if not explored add into visited """


		if(current in nodesVisited):
			pass

		elif(current not in nodesVisited):

			nodesVisited.add(current)


			""" Store the current : parent, cost in parentNodes dictionary """
 

			parentNodes[current]=[pNode,cost]

			""" When the state is not the destination """
			

			if(current!=goal):

				for ChildNode, ChildCost in graph[current].items():
					
					total= PathCost + ChildCost				

					fringe.put((total,ChildNode,current,ChildCost))

					nodesGenerated+=1



			""" When the state is the destination """


			if(current==goal):  
				while current != start: 

					DestinationPath = [] #Used for backtracking to the Origin

					parent = parentNodes[current][0]
					distance = parentNodes[current][1] 

					"""Adding the  current, parent and its distance to route list"""

					DestinationPath.append(current)

					DestinationPath.append(parent) 

					DestinationPath.append(distance)

					route.append(DestinationPath) 
					
					"""The route now containes the parent and its distance. """
					
					current=parentNodes[current][0] 
						
				route.reverse()
				
				
				return route, nodesExpanded, nodesGenerated, PathCost

	return 1 , nodesExpanded, nodesGenerated, PathCost


# Function A* Search which return Solution or Failure 
def InformedSearch(graph,start,goal,h):

	#A priority Queue ordered by path cost 
	fringe=PriorityQueue()

	# An empty set to store the nodes explored
	nodesVisited=set()

	#a list to store the route and parentNodes, to construct the route
	route=[]
	parentNodes={}

	nodesExpanded=0
	nodesGenerated=0
	PathCost=0
	#To keep track of the heuristic cost 
	heuristicCost = 0

	"""
	When the the Origin City is the Destination City 

	"""
	if (start==goal):
		DestinationPath=start
		return 0 , nodesExpanded , nodesGenerated, PathCost , DestinationPath


	fringe.put((heuristicCost,PathCost,start,None,0)) #Add elements into the fringe

	nodesGenerated+=1

	""" loop that keeps running until the fringe becomes empty """
	while not fringe.empty():

		hCost, PathCost,current,pNode,cost = fringe.get()

		nodesExpanded +=1 

		""" Check if the State is explored or not, if not explored add into visited """

		if(current in nodesVisited):
			pass

		elif(current not in nodesVisited):

			nodesVisited.add(current)

			parentNodes[current]=[pNode,cost] 

			""" When the state is not the destination """

			if(current!=goal):

				for ChildNode, ChildCost in graph[current].items():
					
					total= PathCost + ChildCost
					hCost = total + h[ChildNode]

					fringe.put((hCost, total,ChildNode,current,ChildCost))

					nodesGenerated+=1

			""" When the state is not the destination """

			if(current==goal):  
				while current != start: 

					DestinationPath = [] #Used for backtracking

					

					parent = parentNodes[current][0] 			#assigning parent
					distance = parentNodes[current][1] 			#assigning The distance

					#Adding the  current, parent and its distance to route list
					DestinationPath.append(current)

					DestinationPath.append(parent) 

					DestinationPath.append(distance)

					route.append(DestinationPath) 
					
					# The route now containes the parent and its distance.
					#Backtracking the parents

					current=parentNodes[current][0] 
						
				route.reverse()
				
				
				return route, nodesExpanded, nodesGenerated, PathCost

	return 1 , nodesExpanded, nodesGenerated, PathCost




file = open(file,"r")				#Open the InputFile
list_lines = []
lines = file.readlines()
lines.pop()							# remove end of input
for line in lines:
	lines=line.strip().split()
	list_lines.append(lines)

	
	
graph={}						# Empty dict to construct the graph 

"""setting the start node, Goal node and the distance between the nodes."""

for line in list_lines:
	source = line[0]
	destination = line[1]
	nodeCost = line[2]
	
	if source not in graph:
		graph[source] = {}
	if destination not in graph:
		graph[destination] = {}
	graph[source][destination] = float(nodeCost)
	graph[destination][source] = float(nodeCost)

""" When the input is only the origin, Destination and the Input1 """

if(len(sys.argv)==4):
		Value = UninformedSerch(graph,start,goal)
		if(Value[0]==0):
			print("nodes expanded: ",str(Value[1]))
			print("nodes generated: ",str(Value[2]))
			print("distance:",str(Value[3]))
			print("Route: ")


		elif(Value[0]==1):
			print("nodes expanded: ",str(Value[1]))
			print("nodes generated: ",str(Value[2]))
			print("distance:infinity")
			print("Route: None")

		else:
			print("nodes expanded: ",str(Value[1]))
			print("nodes generated: ",str(Value[2]))
			print("distance: %s km" % str(Value[3]))
			print("Route: ")
			for line in Value[0]:
				print("%s to %s , %s km" % (line[1], line[0], line[2]))

""" When the input is the Origin, Destination, the Input1 and the Heuristic """

if(len(sys.argv) == 5):
	hfile=sys.argv[4]
	
	h = open(hfile,"r")

	hlist_lines =[]

	lines_new = h.readlines()
	lines_new.pop()
	for hline in lines_new:
		lines_new=hline.strip().split()
		hlist_lines.append(lines_new)
	

	h_Values = {}

	for v in hlist_lines:
		
		city = v[0]


		heuristic = v[1]
		
		h_Values[city]=float(heuristic)
	
	Value = InformedSearch(graph,start,goal,h_Values)

	if(Value[0]==0):
			print("nodes expanded: ",str(Value[1]))
			print("nodes generated: ",str(Value[2]))
			print("distance:",str(Value[3]))
			print("Route: ")


	elif(Value[0]==1):
		print("nodes expanded: ",str(Value[1]))
		print("nodes generated: ",str(Value[2]))
		print("distance:infinity")
		print("Route: None")

	else:
		print("nodes expanded: ",str(Value[1]))
		print("nodes generated: ",str(Value[2]))
		print("distance: %s km" % str(Value[3]))
		print("Route : ")
		for line in Value[0]:
			print("%s to %s , %s km" % (line[1], line[0], line[2]))



