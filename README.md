# TestCaseGenerator
It gives all the possible model based test cases using the flowchart of the program which is given by the user



In order to do a Model Based Testing, a tester has to know most of the every possible combination 
of inputs that may be given by an end-user. Seeing all the possible inputs using a flowchart is 
hard.

This function, extracts every possible path from a flowchart that contains states and functions 
of a program. This flowchart should be created on draw.io . 

The flowchart should have nodes which represent either a state or function. Nodes should be 
connected with edges with each other.

There has to be one invoke node. All paths should start from the invoke node. Invoke node has to be
rectangle and its value should be 'invoke'. This can be set on draw.io
 
There has to be at least one terminate node. All paths should end in this node. Terminate node has 
to be rectangle and its value should 'terminate'. This can be set on draw.io

A program has functions and states. Functions may be buttons, sliders etc. States and functions are
the main elements of a flowchart.

"Function" in a flowchart appears to be nodes. However, these nodes have to be rectangle on draw.io
and their valus have to be something other than 'invoke' or 'terminate' in order for this program 
to understand the nodes as functions.

"State" in a flowchart appears to be nodes. These nodes have to be ellipse on draw.io
in order for this program to understand those nodes as states.

Every node has at least one child(excluding terminate node), parent or childedge. 
Nodes are connected to each other by edges.

In order to use this program create your flowchart on draw.io and extract it as XML to your computer
and BE SURE TO UNCHECK 'Compressed' BEFORE EXPORTING as XML.

FLOW:
    The main function takes a flowchart in XML format as input.
    Then;
    1- Parse the root of XML file(flowchart) which is created on draw.io 
    2- Exract all nodes and edges drawn on the flowchart
    3- Create a dictionary that acts as a map which allows accessing edge and node objects
        by their Ids
    4- Extract all possible paths from the flowchart excluding the looping edges
    (An edge whose source node and target node are the same is called a looping edge.)
    5- Include the looping edges to the corresponding paths
    6- Report all paths by writing every nodes' value(the value of a node is the text 
    written on it on the flowchart) on a path 
    to a .txt file
