The TAR file consists of three Python 2.7.10 scripts:

1. car_depreciation_loop.py - contains the function that calculates a car's depreciation using a simple loop. To run the script following format should be used:
     python car_depreciation_loop.py <car price>
  Example: 
     python car_depreciation_loop.py 30000 
  Eexpected result:
     Total years to reach 2000 threshold: 26
 If the parameter is not provided the function will finish with error. 

2. car_depreciation_recur.py - contains the function that calculates a car's depreciation using a recursion. To run the script following format should be used:
     python car_depreciation_recur.py <car price>
  Example: 
     python car_depreciation_recur.py 30000 
  Expected result:
     Total years to reach 2000 threshold: 26
 If the parameter is not provided the function will finish with error. 
 
 3. graph.py - contains a script that creates a graph, adds nodes to the graph and creates links (edges) among nodes. To create a sample graph the example picture from the instructions was used. To test the main logic following operations were performed:
    a) Created a graph
    b) Added 6 nodes
    c) Created links among nodes in accordance with the instructions.
    d) Printed all all nodes
  To test the verification logic following operations were performed:
    a) An attempt to insert a duplicate node into the graph
    b) An attempt to create a duplicate link (inserd a duclicate node as a child)
    c) An attempt to create a cycle.
  To run the script following format should be used: 
     python graph.py
  Expected result:
     Node 1 added successfully to the graph
     Node 2 added successfully to the graph
     Node 3 added successfully to the graph
     Node 4 added successfully to the graph
     Node 5 added successfully to the graph
     Node 6 added successfully to the graph
     Node 4 already exists in the graph
     Node 2 successfully inserted as a child of node 1
     Node 3 successfully inserted as a child of node 1
     Node 4 successfully inserted as a child of node 1
     Node 5 successfully inserted as a child of node 2
     Node 3 successfully inserted as a child of node 4
     Node 6 successfully inserted as a child of node 3
     Node 6 successfully inserted as a child of node 4
     Node 6 successfully inserted as a child of node 5
     Node 5 already inserted in node 2 as a child
     A cycle detected. Node 1 will not be inserted as a child of node 6
     A cycle detected. Node 1 will not be inserted as a child of node 5
     1->2,3,4
     2->5
     3->6
     4->3,6
     5->6
     6->No children
    