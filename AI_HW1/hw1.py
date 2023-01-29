
########## Nilüfer TAK ############
######## 2310506  #################

#####The commented codes that did not have any comment about implementations are used for testing purposes.#####


def manhattan_distance(node1,node2): #manhattan distance is basically the difference between row&columns with absolute value
    distance = abs(node1[0]-node2[0]) + abs(node1[1]-node2[1])
    return distance

            
def BFS(graph,minval,start,end):
    visited = [] # List for visited nodes.
    queue = []     #Queue for fringe
    iterator = 0
    visited.append(start) #start with the S node
    queue.append(start) # append S to the fringe

     
    while queue:  #iterate through each node while queue is not empty
        queue.pop(0) #pop the queue each time visiting neighbours
        
        for neighbour in graph:
            if neighbour not in visited:
                visited.append(neighbour) #visit the neighbors as long as min value is not reached
                queue.append(neighbour)
                iterator=iterator+1
                
            
            if iterator >= minval: #The # of visited Cs achieved hence break           
                break
            if len(visited) == len(graph) and minval > iterator+1: #If Cs are finished but still there is not enougn visited nodes that satisfies min value.
                return None
                
                
                               
    visited.append(end) #Cs are finished,lastly visit the final node .      
    
    return visited

     

        
 
        

def UCS(graph,start,end,minval):
    queue =[]  # the fringe is the priority queue
    visited = [] # store which nodes are  visited in order to reach the final node with least cost
    cost = []
    iterator =0
    queue.append([0,start]) #start with S node.
    item=[]
    
    while (len(queue) > 0) and (iterator <minval+2):  #search when queue is not empty meaning there are nodes that can be visited , and until minval is reached.
        queue = sorted(queue)  #sort the queue to pop the last element
        item=queue[-1] # keep value of the last element
        queue.pop(-1) # pop last element 
        item[0] *= -1 #store  cost correctly to add cumulatively in above for loop
        #item[0]-->cost, item[1]--> node index
        current_node =  item[1] #curent node is the next least costly neighbor
        
        if  current_node != end and iterator==minval+1: #if final node is reached append and finish
            
            
            visited.append(end)
            break
            #print(visited)

        
        if (current_node not in visited):   #check if nodes in the queue is not visited and if minval value is not reached yet
            
            for i in range(len(graph)): #visit all neighbors
                
                queue.append( [(item[0] + manhattan_distance(current_node, graph[i]))* -1, graph[i]]) #put the least cumulative cost as priority,first parameter=cost,second parameter=neighbour index
                                                                                                #multiply with -1 so that least costly neighbor will end up at the end of the queue
        
            visited.append(current_node)   # add the visited node to the path
            iterator+=1
    return visited
  
 
       
    



def dfs_helper(visited_dfs,graph,start,dfs_iterator,minval):
    
    if start not in visited_dfs:
        #print (start)
        visited_dfs.append(start) #fringe is the stack called visited_dfs.

        for neighbour in reversed(graph): # I added reversed to get the same output order from shared outputs provided from TAs meaning that deep search's deeper levels are far from start node.
            dfs_iterator=dfs_iterator+1
            if dfs_iterator > minval: # # of visited Cs equal to min value.
                break
            elif len(visited_dfs)==len(graph)-1 and minval+1 > dfs_iterator: # # of visited Cs are lower than min value and graph is finished.
                return None

            else:
                dfs_helper(visited_dfs, graph,neighbour,dfs_iterator,minval) #Visit more Cs and go deep (traversal recursively) in the graph since not enough Cs are visited
    #return visited_dfs   
def DFS(graph,start,end,minval):
    visited_dfs = [] #To keep visited nodes.
    dfs_iterator = 0
    
    
    dfs_helper(visited_dfs,graph,start,dfs_iterator,minval) # Go to recursive traversal.
    
    
    visited_dfs.append(end)
    return visited_dfs # visited Cs are equal to min value.Finally visit the final node and return the result.
        #print(visited_dfs)
    


 
    
def UnInformedSearch(method_name,problem_file_name):
    with open(problem_file_name) as f: #read the given sample txt file.
        wholeinput = f.read()
    
    res =eval(wholeinput) #Parse the input.
    minval=res["min"] #Take the minimum value.
    environment=res["env"] #Take the grid environment.
    envlen=len(environment) #In case I need length of rows&columns of grid.
    
 
    graph = [] #Cs graph.
    start =[] #S point.
    end =[] #F point.
    k=0
    for i in range(0,envlen):
        for j in range(0,envlen):
            if environment[i][j] == 'C': #Put Cs in a graph .
                graph.append([i,j])
                #print(graph[k])
                #k=k+1
            elif environment[i][j] == 'S': #Put S point and F point seperately.
                start.append([i,j])
                #print(start[0])
            elif environment[i][j] == 'F':
                end.append([i,j])
                #print(end[0])
            else:
                continue

    if method_name =="BFS":
        return BFS(graph,minval,start[0],end[0])
    elif method_name =="DFS":
        return DFS(graph,start[0],end[0],minval)
    elif method_name =="UCS":
        ucsgraph =[]
        for i in range(0,envlen):
            for j in range(0,envlen):
                if environment[i][j] == "C" or environment[i][j] == "S" or environment[i][j] == "F":

                    ucsgraph.append([i,j])
        return UCS(ucsgraph,start[0],end[0],minval)        

    
#UnInformedSearch("UCS","sampleproblem1.txt")

