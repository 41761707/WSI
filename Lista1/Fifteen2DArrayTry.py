#Radosław Wojtczak nr indeksu: 254607
#Piętnastka- algorytm A* z dwoma różnymi heurystykami

#shuffle
import random
#queue
from queue import PriorityQueue
#copy
import copy
#sleep
import time
#costam
import numpy
#faster prioQ?
import heapq

class Fifteen:
    def makePermutation(self):
        board=[]
        for i in range(1,self.n*self.m):
            board.append(i)
        board.append(self.n*self.m)
        self.checkPermutation(board)
        return board
    def checkPermutation(self,board):
        permutation=0
        #for i in range(len(board)):
        #    if(board[i]==self.n*self.m):
        #        board[i]=0
        while True:
            random.shuffle(board)
            for i in range(len(board)-2):
                for j in range(i+1,len(board)-1):
                    if(board[i]>board[j] and board[i]!=self.n*self.m and board[j]!=self.n*self.m):
                        permutation=permutation+1
            '''
            For a "15" puzzle to be solvable it has to meet the following:
            1.If the grid width is odd, then the number of inversions in a 
            solvable situation is even.
            2.If the grid width is even, and the blank is on an even row 
            counting from the bottom (second-last, fourth-last etc), 
            then the number of inversions in a solvable situation is odd.
            3.If the grid width is even, and the blank is on an odd row 
            counting from the bottom (last, third-last, fifth-last etc) 
            then the number of inversions in a solvable situation is even.
            A piece is inverted when a bigger number is in front of any 
            amount of smaller numbers.
            '''

            if self.m%2!=0:
                if permutation%2==0:
                    break
            else:
                blankposition=0
                for i in range(self.n*self.m):
                    if(board[i]==self.n*self.m):
                        blankposition=i
                        break
                row=blankposition//4
                print(row)
                if row%2==0:
                    if permutation%2==1:
                        break
                else:
                    if permutation%2==0:
                        break
            print("Wrong permutation")
            permutation=0
        print("Permutations: {}".format(permutation))
    def Printer(self):
        result = ""
        for i in range(len(self.board)):
            result += f"{self.board[i]}" + ("\n" if i % self.m ==self.m-1 else " | ")
        return result

    def startGame(self):
        '''
        boardState = [[0 for x in range(self.n)] for y in range(self.m)]
        j=0
        for i in range(len(self.board)):
            boardState[j][i%self.m]=self.board[i]
            if i%self.m==self.m-1:
                j=j+1
        '''
        boardState=[[1,11,3,5],[12,6,10,4],[9,15,7,2],[13,14,16,8]]
        i,j=self.findBlank(boardState)
        temp=Node(boardState,Node([],None,0,0,0,0),self.distance_heuristic(boardState),self.moveNumber,i,j)
        heapq.heappush(self.queue,temp)
        self.Game(temp)

    def Game(self,temp):
        visited=0
        while(True):

            node=heapq.heappop(self.queue)
            if(node.functionValue==0):
                print("Zwyciestwo")
                print(node)
                print("Liczba ruchow: ",node.moveNumber)
                print("Odwiedzone: ",visited)
                print("Droga: ")
                try:
                    while node.previous!=None:
                        print(node.previous)
                        node=node.previous
                except IndexError:
                    print("Koniec programu")
                break
            visited=visited+1
            if(visited%10000==0):
                print("Visited: ",visited)
            #print("Visited: ",visited)
            #print("Function value: ", node.functionValue)
            #print("Wykonuje ruch numer: {}".format(node.moveNumber))
            #print("Aktualny ruch: ")
            #print(node)
            #print("-------------")
            self.makeAMove(node)
            #time.sleep(10)

    def makeAMove(self,node):
        i=node.blankI 
        j=node.blankJ
        currentBoard=node.board
        previousBoard=node.previous.board
        newNumber=node.moveNumber+1
        if i-1 > -1:
            currentBoard[i][j],currentBoard[i-1][j]=currentBoard[i-1][j],currentBoard[i][j]
            if(currentBoard!=previousBoard):
                #print("TOP")
                #temp.moves.append([currentBoard[i][j],currentBoard[i-1][j]])
                heapq.heappush(self.queue,Node([row[:] for row in currentBoard],node,self.distance_heuristic(currentBoard),newNumber,i-1,j))
            currentBoard[i][j],currentBoard[i-1][j]=currentBoard[i-1][j],currentBoard[i][j]

        if i+1 < self.n:
            currentBoard[i][j],currentBoard[i+1][j]=currentBoard[i+1][j],currentBoard[i][j]
            if(currentBoard!=previousBoard):
                #print("DOWN")
                #temp.moves.append([currentBoard[i][j],currentBoard[i+1][j]])
                heapq.heappush(self.queue,Node([row[:] for row in currentBoard],node,self.distance_heuristic(currentBoard),newNumber,i+1,j))
            currentBoard[i][j],currentBoard[i+1][j]=currentBoard[i+1][j],currentBoard[i][j]

        if j-1 > -1:
            currentBoard[i][j],currentBoard[i][j-1]=currentBoard[i][j-1],currentBoard[i][j]
            if(currentBoard!=previousBoard):
                #print("LEFT")
                #temp.moves.append([currentBoard[i][j],currentBoard[i][j-1]])
                heapq.heappush(self.queue,Node([row[:] for row in currentBoard],node,self.distance_heuristic(currentBoard),newNumber,i,j-1))
            currentBoard[i][j],currentBoard[i][j-1]=currentBoard[i][j-1],currentBoard[i][j]

        if j+1 < self.m:
            currentBoard[i][j],currentBoard[i][j+1]=currentBoard[i][j+1],currentBoard[i][j]
            if(currentBoard!=previousBoard):
                #print("RIGHT")
                #temp.moves.append([currentBoard[i][j],currentBoard[i][j+1]])
                heapq.heappush(self.queue,Node([row[:] for row in currentBoard],node,self.distance_heuristic(currentBoard),newNumber,i,j+1))
            currentBoard[i][j],currentBoard[i][j+1]=currentBoard[i][j+1],currentBoard[i][j]


    def misplaced_heuristic(self,board):
        counter=0
        for i in range(self.n):
            for j in range(self.m):
                if(board[i][j]!=(self.m*i+(j+1))):
                    if(board[i][j]==self.n*self.m):
                        pass
                    else:
                        #print("{} - {}".format(board[i][j],3*i+(j+1)))
                        counter=counter+1
        return counter

    def distance_heuristic(self,board):
        counter=0
        for i in range(self.n):
            for j in range(self.m):
                if(board[i][j]!=self.n*self.m):
                    first,second=self.Distance(board[i][j])
                    counter=counter+abs(first-i)+abs(second-j)
        return counter

    def linear_heuristic(self,board):
        return None

    def findBlank(self,board):
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j]==self.n*self.m:
                    return i,j
    def Distance(self,number):
        first=number//self.n
        second=0
        if(number%self.n==0):
            first=first-1
            second=self.m-1
        else:
            second=number%self.n-1
        return first,second



    def __init__(self,n,m,queue):
        self.n=n
        self.m=m
        self.board=self.makePermutation()
        self.queue=queue
        self.moveNumber=0

    def __str__(self):
        return self.Printer()

class Node:
    def __init__(self,board,previous,functionValue,moveNumber,blankI,blankJ):
        self.board=board
        self.functionValue=functionValue
        self.previous=previous
        self.moveNumber=moveNumber
        self.blankI=blankI
        self.blankJ=blankJ

    def Printer(self):
        #Uwaga tu rozmiary hardcoded
        result=""
        for i in range(4):
            result=result+"{} | {} | {}| {} ".format(self.board[i][0],self.board[i][1],self.board[i][2],self.board[i][3])
            result=result+"\n"
        result=result+"Function value: {}".format(self.functionValue)
        result=result+"\n"
        return result

    def __lt__(self, other):
        #print("LT")
        return self.functionValue < other.functionValue or self.moveNumber < other.moveNumber
        #return self.functionValue+self.moveNumber < other.functionValue + other.moveNumber

    def __gt__(self,other):
        #print("GT")
        return self.functionValue>other.functionValue

    def __le__(self,other):
        #print("LE")
        return self.functionValue<=other.functionValue
    def __ge__(self,other):
        #print("GE")
        return self.functionValue>=other.functionValue

    def __str__(self):
        return self.Printer()



def main():
    print("Working:")
    game=Fifteen(4,4,[])
    print(game)
    game.startGame() 




if __name__=='__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))


'''
Done tests:
#1
board=[[11,10,3,5],[1,12,15,4],[6,14,9,7],[13,8,2,16]]
distance_heuristic: Visited:23491, Moves:64, Time:2.02 s

#2
board=[[2,3,6,12],[10,8,7,4],[9,15,1,5],[13,14,11,16]]
distance_heuristic: Visited:273979, Moves:58, Time:25.8 s
'''