#Class that represents a graph
class MyGraph(object):
    
    def __init__(self):
        #Dictionary that contains all nodes of the graph
        self.nodeList = {}

    #Method that adds a node to the graph
    def addNode(self, newNode):
        
        if newNode.id not in self.nodeList:
            self.nodeList[newNode.id] = newNode
            print 'Node %s added successfully to the graph' % newNode.id
            return True
        else:
            print 'Node %s already exists in the graph' % (newNode.id)
            return False
    #Method that retrieves a node by its id
    def getNodeById(self, id):
        
        if id in self.nodeList:
            return self.nodeList[id]
        else:
            print 'Node %s does not exist' % id
            return None 

    #Method that prints node information by id
    def printNode(self, id):
        
        if id in self.nodeList:
            node = self.nodeList[id]
            print 'Node: id = %s, name = %s' % (node.id, node.name)
        else:
            print 'Node not found'
    
    #Method that prints nodes
    def printAllNodes(self):
        
        for id in sorted(self.nodeList):
            node = self.getNodeById(id)
            node.printChildNodes()

#Class that represents a node
class Node(object):
    
    def __init__(self, id, name):
        
        self.id = id
        self.name = name
        #Dictionary that contains all child nodes of current node
        self.childNodesLst = {}
    
    #This method recursively goes through child nodes to find a cycle
    def isCyclicLink(self, node, id):
        
        childList = node.childNodesLst
        if id in childList:
            return True
        else:
            for k,v in childList.iteritems():
                if self.isCyclicLink(v, id):
                     return True
        return False
    
    #Method that prints all all child nodes of current node
    def printChildNodes(self):
        
        if len(self.childNodesLst) == 0:
            print str(self.id) + '->No children'
        else:
            resLst = []
            res = str(self.id) + '->'
            for k in self.childNodesLst:
                resLst.append(k)
            resLst.sort()
            for i in resLst:
                res = res + str(i) + ','

            print res[0:len(res)-1]
        
    #Method that inserts a child node
    def addChildNode(self, childNode):
        
        if childNode.id not in self.childNodesLst:
            if self.isCyclicLink(childNode, self.id):
                print 'A cycle detected. Node %s will not be inserted as a child of node %s' % (childNode.id, self.id)
                return False
            else:
                self.childNodesLst[childNode.id] = childNode

            self.childNodesLst[childNode.id] = childNode
            print 'Node %s successfully inserted as a child of node %s' % (childNode.id, self.id)
            return True
        else:
            print 'Node %s already inserted in node %s as a child' % (childNode.id, self.id)
            return False
            

#Create a graph 
myGraph = MyGraph()

#Add nodes to the graph
myGraph.addNode(Node(1, 'Node1'))
myGraph.addNode(Node(2, 'Node2'))
myGraph.addNode(Node(3, 'Node3'))
myGraph.addNode(Node(4, 'Node4'))
myGraph.addNode(Node(5, 'Node5'))
myGraph.addNode(Node(6, 'Node6'))

#Attempt to insert a duplicate node
myGraph.addNode(Node(4, 'Node7'))

#Create links
myGraph.getNodeById(1).addChildNode(myGraph.getNodeById(2))
myGraph.getNodeById(1).addChildNode(myGraph.getNodeById(3))
myGraph.getNodeById(1).addChildNode(myGraph.getNodeById(4))
myGraph.getNodeById(2).addChildNode(myGraph.getNodeById(5))
myGraph.getNodeById(4).addChildNode(myGraph.getNodeById(3))
myGraph.getNodeById(3).addChildNode(myGraph.getNodeById(6))
myGraph.getNodeById(4).addChildNode(myGraph.getNodeById(6))
myGraph.getNodeById(5).addChildNode(myGraph.getNodeById(6))

#Attempt to create a duplicate link
myGraph.getNodeById(2).addChildNode(myGraph.getNodeById(5))

#attempt to create a cycle
myGraph.getNodeById(6).addChildNode(myGraph.getNodeById(1))
myGraph.getNodeById(5).addChildNode(myGraph.getNodeById(1))

#Print all nodes
myGraph.printAllNodes()




