In order to do a Model Based Testing, a tester has to know most of the all possible combination 
of user inputs that may be given by a user. Different user input combinations lead to different 
paths. It is desired to be sure that, along these paths, each user input results in the expected
and desired state.

All possible user inputs and their resultant states of the product can be visualized on a 
flowchart. These paths have to be tested so that the tester can be sure that user inputs 
lead to the correct states. However, looking at the flowchart and tracing user inputs and their
resultant states along the paths on flowchart may not be feasible. It may also lead to 
defficiencies in the testing phase.

Keep in mind that a flowchart can also be considered as a graph.

This project extracts every possible path in a graph(flowchart) that contains user inputs and 
their resultant program states. The flowchart should be created on draw.io 

The flowchart should have nodes which represent either a state or a function. Nodes should be 
connected with each other by directed edges(one-way edges).

Inside the graph, there has to be one invoke node. All paths should start from the invoke node. 
Invoke node has to be rectangle and its value should be 'invoke'. This can be set on draw.io
 
Inside the graph, there has to be at least one terminate node. All paths should end in this node. 
Terminate node has to be rectangle and its value should 'terminate'. This can be set on draw.io

Any software has functions(user inputs) and states. Functions may be buttons, sliders etc. 
while a state is the result of a function. States and functions are the main elements of a 
flowchart.

"State" in a flowchart appears to be nodes. However, these nodes have to be rectangle on 
draw.io and their valus have to be something other than 'invoke' or 'terminate' in order for 
this program to perceive the nodes as states.

"Function"(user input) in a flowchart appears to be nodes. These nodes have to be ellipse 
on draw.io in order for this program to perceive those nodes as functions.

Every node has at least one child(excluding terminate node)
Every node has at least one parent(excluding invoke node). 

In order to use this program create your flowchart on draw.io and extract it as XML to your 
computer and BE SURE TO UNCHECK 'Compressed' BEFORE EXPORTING as XML.

IMPORTANT NOTE: CONSIDER THE FLOWCHART YOU CREATE ON draw.io AS A GRAPH. IT IS HIGHLY IMPORTANT
TO CREATE AN ACYCLIC DIRECTED GRAPH ON draw.io . Otherwise, you may encounter with malfunctions.

This script:
    Takes a flowchart as XML format as input.
    Then;
    1- Parses the root of XML file which is created on draw.io 
    2- Exracts all nodes and edges drawn on the flowchart and saves them to nodes and edges lists
    3- Creates a dictionary that acts as a map which allows accessing edge and node objects
        by their Ids
    4- If a node has a parent node, a child node or a child edge, assigns them to the node.
        It also, for every edge, assigns an edge's child node's value to that edge as 
        source value. Same is done for target value.
    5- In flowchart, there may be self looping edges that are edges whose target and source
        nodes are the same. To handle these cases easly and prevent an infinite loop while 
        extracting paths, self looping edges are excluded from edges list and saved in a 
        different list.
    6- Extracts all possible paths in the flowchart graph excluding the self looping edges
    (An edge whose source node and target node are the same is called a self looping edge.)
    7- Includes the self looping edges to the corresponding paths
    8- Reports all paths by writing every nodes' value on a path to a .txt file
