########## Nilüfer TAK ############
######## 2310506  #################

def manhattan_distance(node1,node2): #manhattan distance is basically the difference between row&columns with absolute value
    distance = abs(node1[1]-node2[1]) + abs(node1[0]-node2[0])
    return distance
def UCS(startnode,endnode,graph,rowlen):
    visited = []
    priorityqueue=[]
    priorityqueue.append([0,[startnode[0],startnode[1]]])
    counter=0
    
    while len(priorityqueue)>0:
        
        priorityqueue = sorted(priorityqueue) # sort the priority queue to pop the node with smallest distance
        q=priorityqueue[-1] #pick the node with smallest distance
        priorityqueue.pop(-1) #remove the selected node 
        q[0]*=-1 #remove the selected node's distance value (it was multiplied with -1 to be the last item of priority queue)
        current_node=q[1]
        if [q[1][0],q[1][1]] ==[endnode[0],endnode[1]]:#if the end node is reached,path is found.
            finalpath=[]
            visited.append([endnode[0],endnode[1]])
            for member in reversed(visited): #return mypath as final path where each member is a tuple with (y coordinate,x coordinate)
                road=(member[1],member[0])
                
                finalpath.append(road)
              
            return finalpath#finalpath is in the same format of shared output example.
            


        ##generate neighbors of selected node,q is the selected node
        neighbors=[] #find the current node q's neighbors
        #node has max 4 neighbors left-up-right-down 
        #if node has neighbors with #,do not make it a neighbor
        #only add the neighbors that can be visited i.e. nodes without #
        
        if q[1][0]>0 and q[1][1]>0 and q[1][0] != rowlen-1 and q[1][1] != rowlen-1:
            #left neighbor
            
            if graph[q[1][0]*rowlen+q[1][1]-1][2] != '#':
                neighbors.append([q[1][0],q[1][1]-1])
                
                
            
            #up neighbor
            if graph[(q[1][0]-1)*rowlen+q[1][1]][2] != '#':
                neighbors.append([q[1][0]-1,q[1][1]])
                

            #right neighbor
            if graph[q[1][0]*rowlen+q[1][1]+1][2] != '#':    
                neighbors.append([q[1][0],q[1][1]+1])
                

            #down neighbor
            if graph[(q[1][0]+1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]+1,q[1][1]])
                

        elif q[1][0]==0 and q[1][1]==0:
            #right neighbor
            
            if graph[q[1][0]*rowlen+q[1][1]+1][2] != '#': 
                
                neighbors.append([q[1][0],q[1][1]+1])
                

            #down neighbor
            if graph[(q[1][0]+1)*rowlen+q[1][1]][2] != '#':
                neighbors.append([q[0]+1,q[1][1]])
                

        elif q[1][0]==0 and q[1][1]>0 and q[1][1] != rowlen-1:
            #left neighbor
            
            if graph[q[1][0]*rowlen+q[1][1]-1][2] != '#':
                neighbors.append([q[1][0],q[1][1]-1])
                

            #right neighbor
            if graph[q[1][0]*rowlen+q[1][1]+1][2] != '#': 
                neighbors.append([q[1][0],q[1][1]+1])
                

            #down neighbor
            if graph[(q[1][0]+1)*rowlen+q[1][1]][2] != '#':
                neighbors.append([q[1][0]+1,q[1][1]])



        elif q[1][0]>0 and q[1][1]==0 and q[1][0] != rowlen-1:
            

            #up neighbor
            if graph[(q[1][0]-1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]-1,q[1][1]])
                

            #right neighbor
            if graph[q[1][0]*rowlen+q[1][1]+1][2]!= '#': 
                neighbors.append([q[1][0],q[1][1]+1])
               


            #down neighbor
            if graph[(q[1][0]+1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]+1,q[1][1]])

        elif q[1][0] == rowlen-1 and q[1][1] == 0:
            #up neighbor
            
            if graph[(q[1][0]-1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]-1,q[1][1]])
               
            #right neighbor
            if graph[q[1][0]*rowlen+q[1][1]+1][2] != '#': 
                
                neighbors.append([q[1][0],q[1][1]+1])

        elif q[1][0] == rowlen-1 and q[1][1] != 0 and q[1][1] != rowlen-1:
            #left neighbor
            
            if  graph[q[1][0]*rowlen+q[1][1]-1][2] != '#':
                neighbors.append([q[1][0],q[1][1]-1])
                
            
            #up neighbor
            if graph[(q[1][0]-1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]-1,q[1][1]])
                

            #right neighbor
            if graph[q[1][0]*rowlen+q[1][1]+1][2] != '#': 
                neighbors.append([q[1][0],q[1][1]+1])
                

        elif q[1][1] == rowlen-1 and q[1][0] == 0:
            #left neighbor
            
            if graph[(q[1][0]-1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]-1,q[1][1]])
                

            #down neighbor
            if graph[(q[1][0]+1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]+1,q[1][1]])
                

        elif q[1][1] == rowlen-1 and q[1][0] != 0 and q[1][0] != rowlen-1:
            
            #left neighbor
            if graph[q[1][0]*rowlen+q[1][1]-1][2] != '#':
                
                neighbors.append([q[1][0],q[1][1]-1])
                
            #up neighbor
            if graph[(q[1][0]-1)*rowlen+q[1][1]][2] != '#':
                neighbors.append([q[1][0]-1,q[1][1]])
                

            #down neighbor
            if graph[(q[1][0]+1)*rowlen+q[1][1]][2] != '#':
                
                neighbors.append([q[1][0]+1,q[1][1]])

        elif q[1][1] == rowlen-1 and q[1][0] == rowlen-1:
            
            #left neighbor
            if graph[q[1][0]*rowlen+q[1][1]-1][2] != '#':
                
                neighbors.append([q[1][0],q[1][1]-1])
                
            
            #up neighbor
            if graph[(q[1][0]-1)*rowlen+q[1][1]][2] != '#':
                neighbors.append([q[1][0]-1,q[1][1]])
        
        if current_node not in visited:
            #visit all the neighbors of selected node
            for successor in neighbors:
                
                priorityqueue.append([(q[0]+manhattan_distance(current_node, successor))* -1,[successor[0],successor[1]]])#calculate each successor's distance values and put into priority queue
            visited.append(q[1])                                                                      #multiply with -1 so that the least costly neighbor will end up at the end of the queue
    
    
    


def AStar(startnode,endnode,graph,rowlen):
    #nodes (x,y,heuristic or S or E or #)
    openList=[] #list that has nodes possible to be selected
    closeList=[] #list that has nodes which are selected and evaluated their f value
    startnode=list(startnode)#make startnode a list so that its f value can be added
    startnode.pop(2) #remove the start node's 'S' as an h value
    startnode.insert(2,0) #initialize startnode h value to 0 to avoid string comparisons
    startnode.insert(3,0)#initialize its g value as 0
    startnode.insert(4,0)#initialize its f value as 0
    startnode.insert(5,0)#startnode has no parent hence initialize its parent to 0.
    openList.append(startnode) #add start node to openList
    q=0 #a variable to hold the current node
    qg=0
    successorf=0 #a variable to put f values of nodes
    notforget=[] #the list to calculate the final path
    notforget.append(startnode)
    while len(openList): #if len(openList)==0 , solution has not been found.
        minvalue=100000
        #openedList members has [x coordinate,y coordinate,heuristic value,g value,f value] as a list
        for i in range(0,len(openList)): #find the node with smallest f in openedList
            
            if openList[i][4] < minvalue and openList[i][2]!='#':
                minvalue=openList[i][4]
                q=openList[i]  #node with the least f #3a
                
                q=list(q)
                
                
        
        openList.remove(q) #remove the node with smallest f from openedList
        closeList.append(q) #add the node with smallest f to closedList
        # q has ((x,y,heuristic or s or e or #),f)
        
        if q[0]==endnode[0] and q[1]==endnode[1]: #if current node is target node E,break from while loop,path is found.
            mypath=[]
            finalpath=[]
            mypath.append([q[0],q[1]])
            thenode=[]
            forendnode=0
            while True:
                for i in range(0,len(closeList)):
                    if forendnode!=0: #if start node is reached then break
                        break
                    
                    if [closeList[i][0],closeList[i][1]]==[q[5][0],q[5][1]]:
                        thenode=closeList[i]
                        mypath.append([thenode[0],thenode[1]])
                        q=closeList[i]
                        if [q[0],q[1]]==[startnode[0],startnode[1]]:
                            forendnode+=1
                            
                if forendnode!=0: #start node is reached , go to return to finalpath            
                    break            


                    

                       
            for member in mypath: #return mypath as final path where each member is a tuple with (y coordinate,x coordinate)
                road=(member[1],member[0])
                
                finalpath.append(road)
            return finalpath#finalpath is in the same format of shared output example.
            
            
        
        neighbors=[] #find the current node q's neighbors
        #node has max 4 neighbors left-up-right-down 
        #if node has neighbors with #,do not make it a neighbor
        #only add the neighbors that can be visited i.e. nodes without #
        if q[0]>0 and q[1]>0 and q[0] != rowlen-1 and q[1] != rowlen-1:
            #left neighbor
            
            if graph[q[0]*rowlen+q[1]-1][2] != '#':
                neighbors.append([q[0],q[1]-1,graph[q[0]*rowlen+q[1]-1][2]])
                
                
            
            #up neighbor
            if graph[(q[0]-1)*rowlen+q[1]][2] != '#':
                neighbors.append([q[0]-1,q[1],graph[(q[0]-1)*rowlen+q[1]][2] ])
                

            #right neighbor
            if graph[q[0]*rowlen+q[1]+1][2] != '#':    
                neighbors.append([q[0],q[1]+1,graph[q[0]*rowlen+q[1]+1][2]])
                

            #down neighbor
            if graph[(q[0]+1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]+1,q[1],graph[(q[0]+1)*rowlen+q[1]][2]])
                

        elif q[0]==0 and q[1]==0:
            #right neighbor
            
            if graph[q[0]*rowlen+q[1]+1][2] != '#': 
                
                neighbors.append([q[0],q[1]+1,graph[q[0]*rowlen+q[1]+1][2]])
                

            #down neighbor
            if graph[(q[0]+1)*rowlen+q[1]][2] != '#':
                neighbors.append([q[0]+1,q[1],graph[(q[0]+1)*rowlen+q[1]][2]])
                

        elif q[0]==0 and q[1]>0 and q[1] != rowlen-1:
            #left neighbor
            
            if graph[q[0]*rowlen+q[1]-1][2] != '#':
                neighbors.append([q[0],q[1]-1,graph[q[0]*rowlen+q[1]-1][2]])
                

            #right neighbor
            if graph[q[0]*rowlen+q[1]+1][2] != '#': 
                neighbors.append([q[0],q[1]+1,graph[q[0]*rowlen+q[1]+1][2]])
                

            #down neighbor
            if graph[(q[0]+1)*rowlen+q[1]][2] != '#':
                neighbors.append([q[0]+1,q[1],graph[(q[0]+1)*rowlen+q[1]][2]])



        elif q[0]>0 and q[1]==0 and q[0] != rowlen-1:
            

            #up neighbor
            if graph[(q[0]-1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]-1,q[1],graph[(q[0]-1)*rowlen+q[1]][2]])
                

            #right neighbor
            if graph[q[0]*rowlen+q[1]+1][2]!= '#': 
                neighbors.append([q[0],q[1]+1,graph[q[0]*rowlen+q[1]+1][2]])
               


            #down neighbor
            if graph[(q[0]+1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]+1,q[1],graph[(q[0]+1)*rowlen+q[1]][2]])

        elif q[0] == rowlen-1 and q[1] == 0:
            #up neighbor
            
            if graph[(q[0]-1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]-1,q[1],graph[(q[0]-1)*rowlen+q[1]][2]])
               
            #right neighbor
            if graph[q[0]*rowlen+q[1]+1][2] != '#': 
                
                neighbors.append([q[0],q[1]+1, graph[q[0]*rowlen+q[1]+1][2]])

        elif q[0] == rowlen-1 and q[1] != 0 and q[1] != rowlen-1:
            #left neighbor
            
            if  graph[q[0]*rowlen+q[1]-1][2] != '#':
                neighbors.append([q[0],q[1]-1,graph[q[0]*rowlen+q[1]-1][2]])
                
            
            #up neighbor
            if graph[(q[0]-1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]-1,q[1],graph[(q[0]-1)*rowlen+q[1]][2]])
                

            #right neighbor
            if graph[q[0]*rowlen+q[1]+1][2] != '#': 
                neighbors.append([q[0],q[1]+1,graph[q[0]*rowlen+q[1]+1][2]])
                

        elif q[1] == rowlen-1 and q[0] == 0:
            #left neighbor
            
            if graph[(q[0]-1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]-1,q[1],graph[(q[0]-1)*rowlen+q[1]][2]])
                

            #down neighbor
            if graph[(q[0]+1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]+1,q[1],graph[(q[0]+1)*rowlen+q[1]][2]])
                

        elif q[1] == rowlen-1 and q[0] != 0 and q[0] != rowlen-1:
            
            #left neighbor
            if graph[q[0]*rowlen+q[1]-1][2] != '#':
                
                neighbors.append([q[0],q[1]-1,graph[q[0]*rowlen+q[1]-1][2]])
                
            #up neighbor
            if graph[(q[0]-1)*rowlen+q[1]][2] != '#':
                neighbors.append([q[0]-1,q[1],graph[(q[0]-1)*rowlen+q[1]][2]])
                

            #down neighbor
            if graph[(q[0]+1)*rowlen+q[1]][2] != '#':
                
                neighbors.append([q[0]+1,q[1],graph[(q[0]+1)*rowlen+q[1]][2]])

        elif q[1] == rowlen-1 and q[0] == rowlen-1:
            
            #left neighbor
            if graph[q[0]*rowlen+q[1]-1][2] != '#':
                
                neighbors.append([q[0],q[1]-1,graph[q[0]*rowlen+q[1]-1][2]])
                
            
            #up neighbor
            if graph[(q[0]-1)*rowlen+q[1]][2] != '#':
                neighbors.append([q[0]-1,q[1],graph[(q[0]-1)*rowlen+q[1]][2]])

        
            
        for successor in neighbors: #for every neighbor of the current node which is called successor
            
            counter=0
            counter2=0
            counter3=0
            counter4=0
            for k in range(0,len(closeList)):
                if [successor[0],successor[1]] == [closeList[k][0],closeList[k][1]] and counter3<1:
                    counter3 += 1 #if the node is already visited and calculated,ignore the node(successor).
            if counter3 !=0:
                continue
            else: #if is not on closed list,find the successor's g and f value
                #right now,successor has x,y coordinate and h value,first add g value to successor,then f.
                # h value is hold as a string i.e. h value is '3' hence it is needed to be int to calculate g value.
                successor.insert(3,int(q[3])+1) #g value is equal to predecessor node's g value and the distance between neighbor and current node which is always 1.
                if successor[2]=='E':
                    successor[2]=0 #since E has no heuristic value , if E is a successor , in order to calculate g ,change its h value to 0 instead of 'E' to avoid invalid string literal.
                successor.insert(4,int(successor[2])+successor[3]) # f value is equal to g value + h value of the node.
            
                #Now, successor has [x coordinate,y coordinate,h value,g value,f value]
                if len(openList) ==0: # this is  only for the start node since we popped from the open list in the begining
                    openList.append(q)#in order to make start node's children having parent,the start node is appended temporarily 
                for i in range(0,len(openList)):
                    if [successor[0],successor[1]]!=[openList[i][0],openList[i][1]] and counter<1: #if successor not open list,add its parent as current node
                        successor.insert(5,[q[0],q[1]])
                        counter += 1
                    elif [successor[0],successor[1]]==[openList[i][0],openList[i][1]] and successor[4]<openList[i][4] and counter2<1: # if successor is in the openlist but with smaller f,then replace its parent as current node. 
                        successor.insert(5,[q[0],q[1]])
                        counter2 += 1

                for i in range(0,len(openList)): #if successor is already on the openlist but has bigger f value ignore it with counter4 
                    if  [successor[0],successor[1]]==[openList[i][0],openList[i][1]]  and successor[4]>openList[i][4]:#and if it has bigger f value,skip this successor.
                        counter4 +=1
                         
                    
                if counter4 !=0:#proceed with the next neighbor
                    continue             
                   
                
                openList.append(successor)
                if len(openList) ==2 and openList[0][2]==0:#this is only for start node's first child to have a parent.
                    openList.pop(0)  #after first child has a parent,start node is not needed to be on the openList.                             
        
       

        
def InformedSearch(method_name,problem_file_name ):

    with open(problem_file_name) as f: #read the given sample txt file.
        wholeinput = f.read()

  
    graph=[] #graph includes indexes with their heuristic values  
    k=0
    s=0    
    arr = wholeinput.split()
    rowlen=int(len(arr)**0.5)

    for i in range(0,rowlen):#hold start node and end node's coordinates.
        for j in range(0,rowlen):
            if arr[k]=='S': 
                startnode=[i,j,arr[k]]
            if arr[k]=='E':    
                endnode=[i,j,arr[k]]
            k+=1
    for x in range(0,rowlen):
        for y in range(0,rowlen):
            if arr[s]=='S' or arr[s]=='E': #initialize start node and end node's h value as 0 to avoid string comparisons.
                graph.append([x,y,0])
            else:

                graph.append([x,y,arr[s]])
            s+=1
    if method_name=='AStar':
        return AStar(startnode,endnode,graph,rowlen)
    elif method_name=='UCS':
        return UCS(startnode,endnode,graph,rowlen)    




   
