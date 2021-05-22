#!/usr/bin/env python
# coding: utf-8


from queue import Queue

witness=[]                            # global variable used to record any witness for violation of bipartite graphs

'''
BFS travel using queue and adjuscency list
'''
def BFSVisit(q, adjL):                
    while q.empty()==False:           # Do breadth first search until the queue is empty
        
        i=q.get()                     # dequeue
        if adjL[i][-1]==1:            # Determine color of neighbouring vertices of i
            nColor = 2                # if i.color=Black (1), then neigboring vertex color=Green (2)
        else:                         # else if i.color=Green (2), then neigboring vertex color=Black (1)
            nColor = 1
        for v in adjL[i][0:-1]:       # explore each edge out of the current node at index i
            v -= 1                    # adjust for index in adjuscency matrix : vertex 1 is stored at index 0
            if adjL[v][-1]==0:        # if vertex v is white i.e. unvisited, then color v and enqueue
                adjL[v][-1]=nColor
                q.put(v)
            elif adjL[v][-1]!=nColor: # if v is already in the same color as i, then not a bipartite graph 
                global witness
                witness=i,v           # record the adjucent vertices in same color as witness
                return -1
    return 0    


'''
Keep two partitions of the bipartite graph in two tuples, and return them
'''
def get_biPartitions(adjL):           
    
    black=[]                          # vertices with color black will be kept here
    green=[]                          # vertices with color green will be kept here

    for i in range(len(adjL)):        # for each vertex, look at the color and put in correct list
        if adjL[i][-1]==1:
            black.append(i+1)
        elif adjL[i][-1]==2:
            green.append(i+1)
    return tuple(black),tuple(green)  # return as tuples, for printing


'''
Main function to take inputs and determine if the graph is bipartite
'''

if __name__=='__main__':

    n=int(input())                      # read number of vertices from input line 1          
    adjL=[[] for _ in range(n)]         # initialise adjacency list with length as number of vertices
    for i in range(n):                  # store adjacency list from next n input lines
        adjL[i]=list(map(int,input().split()))
        
    for i in range(n):
        adjL[i].append(0)               # 0 : White. Color each vertex in white.

    q=Queue(maxsize=n)                  # initialise max size of queue as number of vertices

    for i in range(n):
        if adjL[i][-1]==0:              # Perform BFS traversal for each unvisited vertex (i.e. vertex of color white).
            adjL[i][-1]=1               # 1: Black. The vertex is coloured black
            q.put(i)                    # enqueue vertex for BFS search
            rc=BFSVisit(q,adjL)         # perform breadth first search
            if rc==-1:                  # if discrepencies found, print the witness, along with the partitions done before discrepency
                black,green=get_biPartitions(adjL)
                print("No ",witness, " are adjacent vertices in bi partitions ", black,green)
                break

    if rc==0:                              # if no discrepencies found from any of the BFS searches 
        black,green=get_biPartitions(adjL) # get the partitions of the bipartite graph, and print
        print("Yes ",black,green)

