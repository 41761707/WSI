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
        while True:
            random.shuffle(board)
            for i in range(len(board)):
                for j in range(i+1,len(board)):
                    if(board[i]==self.n*self.m or board[j]==self.n*self.m):
                        continue
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
        print(self.board)
        heapq.heappush(self.queue,Node(self.board,self.distance_heuristic(self.board),self.moveNumber,Node([],0,0,None)))
        visited=0
        while(True):

            node=heapq.heappop(self.queue)
            if(node.functionValue==0):
                print("Zwyciestwo")
                print(node)
                print("Liczba ruchow: ",node.moveNumber)
                print("Odwiedzone: ",visited)
                print("Droga: ")
                while node.previous!=None:
                    print(node)
                    node=node.previous
                break
            visited=visited+1
            if(visited==4000000):
                print("Stop")
                break
                #print("Visited: ",visited)
                #print("Function value: ", node.functionValue)
                #print("Wykonuje ruch numer: {}".format(node.moveNumber))
                #print("Aktualny ruch: ")
                #print(node)
                #print("-------------")
            self.makeAMove(node)
            #time.sleep(10)

    def makeAMove(self,node):
        board=node.board
        newNumber=node.moveNumber
        #newVisited=[row[:] for row in node.visited]
        #newVisited.append(board)
        for i in range(len(board)):
            if(board[i]==self.n*self.m):
                #up
                if i//self.n>0:
                    #print("UP")
                    newBoard=board[:]
                    newBoard[i],newBoard[i-self.n]=newBoard[i-self.n],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))
                #down
                if i//self.n<self.n-1:
                    #print("DOWN")
                    newBoard=board[:]
                    newBoard[i],newBoard[i+self.n]=newBoard[i+self.n],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))
                #left
                if (i-1)//self.n == i//self.n:
                    #print("LEFT")
                    newBoard=board[:]
                    newBoard[i], newBoard[i-1]=newBoard[i-1],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))

                #right
                if(i+1)//self.n==i//self.n:
                    #print("RIGHT")
                    newBoard=board[:]
                    newBoard[i],newBoard[i+1]=newBoard[i+1],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))



    def misplaced_heuristic(self,board):
        counter=0
        for i in range(self.m*self.n):
            if(board[i]==self.n*self.m):
                continue
            if(board[i]!=i):
                counter=counter+1
        return counter
    def distance_heuristic(self,board):
        counter = 0
        for i in range(self.m*self.n):
            if board[i] == self.m*self.n:
                continue
            row,column=self.Distance(board[i])
            counter=counter+abs(row-(i//self.n))+abs(column-(i%self.m))
        #print(counter)
        return counter

    def linear_heuristic(self,board):
        manhattan=self.distance_heuristic(board)
        conflict=0

        for row in range(self.n):
            for i in range(self.m):
                for j in range(i+1,self.m):
                    if(board[row*self.m+i]!= self.m*self.n and board[row*self.m+j]!=self.m*self.n):
                        if(board[row*self.m+i] > board[row*self.m+j]):
                            row_destination_i,_=self.Distance(board[row*self.m+i])
                            row_destination_j,_=self.Distance(board[row*self.m+j])
                            if(row_destination_i==row and row_destination_j==row):
                                conflict=conflict+1
        for column in range(self.m):
            for i in range(self.n):
                for j in range(i+1,self.n):
                    if(board[i*self.m+column]!= self.m*self.n and board[j*self.m+column]!=self.m*self.n):
                        if(board[i*self.m+column]>board[j*self.m+column]):
                            _,column_destination_i=self.Distance(board[i*self.m+column])
                            _,column_destination_j=self.Distance(board[j*self.m+column])
                            if(column_destination_i==column and column_destination_j==column):
                                conflict=conflict+1
        return manhattan+2*conflict




    def Distance(self,number):
        first=number//self.n
        second=0
        if(number%self.n==0):
            first=first-1
            second=self.m-1
        else:
            second=number%self.n-1
        return first,second



    def __init__(self,n,m):
        self.n=n
        self.m=m
        self.board=[4,2,3,7,1,6,12,8,15,9,10,11,16,5,13,14]
        self.seen=set()
        self.queue=[]
        self.moveNumber=0

    def __str__(self):
        return self.Printer()

class Node:
    def __init__(self,board,functionValue,moveNumber,previous):
        self.board=board
        self.functionValue=functionValue
        self.moveNumber=moveNumber
        self.previous=previous
    def Printer(self):
        result = ""
        for i in range(len(self.board)):
            result += f"{self.board[i]}" + ("\n" if i % 4 == 3 else " | ")
        result=result+"Move number: "+str(self.moveNumber)+"\n"
        return result

    def __lt__(self, other):
        return self.functionValue +self.moveNumber < other.functionValue + other.moveNumber

    def __str__(self):
        return self.Printer()



def main():
    print("Working:")
    game=Fifteen(4,4)
    print(game)
    game.startGame() 




if __name__=='__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))


'''
Done tests:
#1
board=[14, 5, 12, 3, 13, 1, 9, 11, 16, 7, 8, 4, 2, 10, 6, 15]
distance_heuristic: Visited:592552, Moves:46, Time:46.89s
linear_heuristic: Visited:399793, Moves:46, Time:112.1s
#2
board=[1,3,16,15,5,7,11,4,9,2,8,12,13,10,14,6]
distance_heuristic: Visited:11273, Moves:30, Time:0.79s
linear_heuristic: Visited:8025, Moves:32, Time:2.10s
#3
board=[2,5,1,3,6,8,11,12,16,9,7,14,13,10,15,4]
distance_heuristic: Visited:30751, Moves:34, Time:2.15s
linear_heuristic: Visited:7007, Moves:34, Time:1.65s
#4
board=[13,1,2,10,5,3,11,7,9,6,16,8,14,15,4,12]
distance_heuristic: Visited:87411, Moves:36, Time:7.24s
linear_heuristic: Visited:15520 ,Moves:36 ,Time:3.81s
#5
board=[14,1,2,8,5,6,4,3,9,7,11,10,13,12,16,15]
distance_heuristic: Visited:10099, Moves:31, Time:0.71s
linear_heuristic: Visited:3683 ,Moves:31 ,Time:0.93s
#6
board=[8,1,7,3,13,10,6,5,2,15,14,4,9,16,11,12]
distance_heuristic: Visited:143005, Moves:40, Time:11.35s
linear_heuristic: Visited:40519 ,Moves:40 ,Time:11.01s
#7
board=[12, 14, 8, 9, 6, 4, 2, 10, 15, 16, 3, 11, 5, 13, 1, 7]
distance_heuristic: Visited:3018170, Moves:55, Time:255.0s
linear_heuristic: Visited:1480419, Moves:55, Time:421.1s
#8
board=[14, 13, 2, 11, 4, 6, 5, 10, 3, 1, 16, 8, 7, 15, 9, 12]
distance_heuristic: Visited:1906763, Moves:52, Time:152.9s
linear_heuristic: Visited:552249, Moves:52, Time:149.5s
#9
board=[2,10,7,3,1,5,6,9,13,14,11,4,16,15,12,8]
distance_heuristic: Visited:13886, Moves:33, Time:0.96s
linear_heuristic: Visited:5933 ,Moves:33 ,Time:1.71s
#10
board=[5,8,6,12,10,16,13,14,3,9,1,2,4,11,15,7]
distance_heuristic: Visited:507118 , Moves:52 , Time:42.3s
linear_heuristic: Visited:231267 , Moves:52 , Time:62.6s
#11
board=[4, 2, 3, 7, 1, 6, 12, 8, 15, 9, 10, 11, 16, 5, 13, 14]
distance_heuristic: Visited:252538 ,Moves:39 ,Time:20.7s
linear_heuristic: Visited:7565, Moves:37, Time:1,82s
'''