###### NİLÜFER TAK #######
#####  2310506 ########
def possible_moves(move): #generates game tree
    mylist=[]
    for pile, objects in enumerate(move): #pile=which pile is the current i.e move[0],move[1]...,objects=# of objects in that pile
        #print(pile,counters)
        for left in range(objects):#take all possible object picks for that pile  
            #print(left)
            mylist.append(move[:pile] + (left,) + move[pile + 1 :]) #in order to make mylist looks similar to this:[(0, 3, 5), (1, 0, 5), (1, 1, 5), (1,2, 5), (1, 3, 0), (1, 3, 1), (1, 3, 2), (1, 3, 3), (1, 3, 4)]
    return mylist

def game_finished(move,maxplayer):   
    counter=0
    for i in move:
        if i==0:
            counter+=1 #each move has number of objects in each pile,check if in each pile there are any objecs left or not i.e move[0]=0 ,move[1]=0,move[2]=0 ....
            
    if counter==len(move): #if there are no objects in any of the pile ,move is finished
        if maxplayer: #since max player's score is asked,if no pile is left and it is max's turn ,that means min took the last object hence max wins
            return 1 #return 1 since max won
        else:
            return -1 #return -1 when min wins   
          
def value(processed_nodes,move, maxplayer):
    scores=[]#keep the scores of min and max player
    
    result=game_finished(move, maxplayer)
    if result is not None: #if there are stil moves to play , return result of the move
        return result,processed_nodes
    
    if maxplayer: #if max's turn take max valued move
        for successor in possible_moves(move):#calculate each possible moves result and processed nodes
            processed_nodes+=1#keep the number of visited nodes for each move
            fst, processed_nodes=value( processed_nodes,successor,False)#now,it's min's turn
            scores.append(fst)

        return max(scores), processed_nodes    #return the max score for max player
    else: #if min's turn take min valued move
        for successor in possible_moves(move): #calculate each possible moves result and processed nodes
            processed_nodes+=1
            fst, processed_nodes=value(processed_nodes,successor,True)#now,it's max's turn
            scores.append(fst)
                
        return min(scores), processed_nodes  #return the min score for min player
     


def minimax(moves): 
    
    for best_move in possible_moves(moves):
        score,nodes = value(0,best_move,False)#get the best score result with the # of processed nodes 
        if score > 0:#since the aim is to find best move for max player,the score must be 1 i.e bigger than 0
            break 
    return best_move,nodes    
          


def pruning(processed_nodes,move, maxplayer, alpha=-1, beta=1):
    scores = []
    result=game_finished(move ,maxplayer)

    if result is not None:#if there are stil moves to play , return result of the move
        return result,processed_nodes

    
    for new_move in possible_moves(move):
        processed_nodes+=1#keep the processed nodes for each move
        score,processed_nodes = pruning(processed_nodes,new_move, not maxplayer,alpha, beta)#next player's turn
        
        scores.append(score)
        
        if maxplayer:
            alpha = max(alpha, score) #a=max(a,v) where v is the score found above
        else:
            beta = min(beta, score)#b=min(b,v) where v is the score found above
        if beta <= alpha:
            break
    if maxplayer:#if it's maxplayer's turn,return max score 
        return max(scores),processed_nodes #maxplayer's best option on path to root
    else:#if it's minplayer's turn,return min score 
        return min(scores),processed_nodes  #minplayer's best option on path to root      
    
def alphabeta(moves): 
    
    for best_move in possible_moves(moves):
        score,nodes= pruning(0,best_move,False)#get the best move result with the # of visited nodes 
        if score > 0:#since the aim is to find best move for max player,the score must be 1 i.e bigger than 0
            break
    return best_move,nodes

        
def SolveGame ( method_name , problem_file_name , player_type ):
    with open(problem_file_name) as f:#get the input
        lines = f.readlines()
        input=tuple(eval(lines[0])) #read it and convert to tuple to match the output format
        

        if player_type =='MAX':#since "For the nim games only the max-player (X, player type="MAX") is going to be tested" as stated in the homework pdf
            if method_name =='AlphaBeta':
                result=alphabeta(input)
                return list(result)#to match the output format
                
            elif method_name =='Minimax': 
                result= minimax(input)
                return list(result)  #to match the output format


            

        

