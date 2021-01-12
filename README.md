# Route-Between-2-Cities


![alt text](https://github.com/span97/Route-Between-2-Cities/blob/main/route.png)


Code Structure :

The code take input from the User and first assigns the arguments and checks which function to perform based on the number of arguments passed by the user.

*Reading the file :
	 The file is read and a dictionary (graph) is created which contains the city as the key and it 	possible child and its distances as children, hence getting the Origin, Goal and the input file.

*Uniformed Search :

	If there are 4 arguments, then Uninformed Search takes place. 
	The uninformed function takes parameters as Origin, Goal and the input file.

In order to find the optimal path  uniformed cost search Algorithm is used to find the route. 

--> It checks the following conditions:

	If the source is the goal and returns.

	If current node not destination, expand its children till the goal Is reached.
		** The path cost is the current node cost + Cost of the child

	And keep checking if are nodes visited, if so pass, else add into the list.

-->To get the route : 

	Using the goal and the parent nodes that are stored we back track to the origin and reverse to get 	the route.


>>Here Priority Queue is used in the fringe to get the optimal route based on the path cost.

*Uniformed Search :
	If there are 5 arguments, then Uninformed Search takes place. 
	* The heuristic file is also made into a dictionary with each city being the key and its distance as 	value.

	The informed function takes parameters as Origin, Goal , the input file and the h_file

In order to find the optimal path  A* Algorithm is used to find the route. 

The Informed Search function is almost to the Uniformed search, major difference is how the path cost is searched.

Here the path-cost that determines the fringe is :
		--> current node cost + child node cost + its heuristic value. 

>>Here Priority Queue is used in the fringe to get the optimal route based on the path cost.



INSTRUCTIONS TO RUN :

Running in command prompt- in the right directory of where the files are stored.
3 files :

find_route.py - contains the source code

Input1.txt - input file with the city destination distance 

h_file.txt - is the heuristic file.


---find_route.py input_filename origin_city destination_city heuristic_filename---

For Uninformed Search :
		
		python3 find_route.py input1.txt Bremen Kassel 

Where input1.txt is the input file with the city destination distance

For Informed Search :

		python3 find_route.py input1.txt Bremen Kassel h_file.txt


Where input1.txt is the input file with the city destination distance.

Where h_file.txt is the heuristic file.









