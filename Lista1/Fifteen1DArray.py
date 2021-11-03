#Radosław Wojtczak nr indeksu: 254607
#Piętnastka- algorytm A* z dwoma różnymi heurystykami

#shuffle
import random
#copy
import copy
#sleep
import time
#faster prioQ?
import heapq


#Klasa odpowiedzialna za przeprowadzenie rozgrywki
class Fifteen:
    '''
    Funkcja odpowiedzialna za przygotowanie planszy
    @return board- przygotowana plansza
    '''
    def makePermutation(self):
        board=[]
        #Początkowo plansza jest postaci [1,2,...,n]
        for i in range(1,self.n*self.m):
            board.append(i)
        board.append(self.n*self.m)
        #Uruchomienie funkcji sprawdzającej poprawność
        self.checkPermutation(board)
        return board

    '''
    Funkcja odpowiedzialna za przygotowanie rozwiązywalnej łamigłówki
    @param board- tablica przedstawiająca planszę
    '''
    def checkPermutation(self,board):
        #Zmienna przechowująca liczbę permutacji
        permutation=0
        #Obliczanie liczby permutacji zgodnie z rozuowaniem podanym w sprawozdaniu
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

    '''
    Funkcja odpowiedzialna za przejrzyste przedstawienie planszy
    @return result- reprezentacja planszy
    '''
    def Printer(self):
        result = ""
        for i in range(len(self.board)):
            result += f"{self.board[i]}" + ("\n" if i % self.m ==self.m-1 else " | ")
        return result


    #Funkcja odpowiedzialna za uruchomienie, przeprowadzenie oraz poprawne zakończenie
    #rozgrywki
    def startGame(self):
        print(self.board)
        heapq.heappush(self.queue,Node(self.board,self.distance_heuristic(self.board),self.moveNumber,Node([],0,0,None)))
        #zmienna przechowujaca liczbe odwiedzonych stanów
        visited=0
        while(True):

            node=heapq.heappop(self.queue)
            #Jeśli wartość funkcji heurystycznej jest równa 0-sukces
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
            #Ograniczenie ze względu na pamięć
            #w sytuacjach, gdyby ułożenie było zbyt pamięciochłonne
            if(visited==4000000):
                print("Stop")
                break
                #print("Visited: ",visited)
                #print("Function value: ", node.functionValue)
                #print("Wykonuje ruch numer: {}".format(node.moveNumber))
                #print("Aktualny ruch: ")
                #print(node)
                #print("-------------")
            #Wywołanie funkcji odpowiedzialnej za przemieszczanie się
            #po grafie stanów
            self.makeAMove(node)
            #time.sleep(10)

    '''
    Funkcja odpowiedzialna za przemieszczanie się po grafie stanów
    @param node- aktualnie rozpatrywany stan
    '''
    def makeAMove(self,node):
        board=node.board
        newNumber=node.moveNumber
        #newVisited=[row[:] for row in node.visited]
        #newVisited.append(board)
        for i in range(len(board)):
            if(board[i]==self.n*self.m):
                #Czy można do góry
                if i//self.n>0:
                    #print("UP")
                    newBoard=board[:]
                    newBoard[i],newBoard[i-self.n]=newBoard[i-self.n],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))
                #Czy można do dołu
                if i//self.n<self.n-1:
                    #print("DOWN")
                    newBoard=board[:]
                    newBoard[i],newBoard[i+self.n]=newBoard[i+self.n],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))
                #Czy można na lewo
                if (i-1)//self.n == i//self.n:
                    #print("LEFT")
                    newBoard=board[:]
                    newBoard[i], newBoard[i-1]=newBoard[i-1],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))

                #Czy można na prawo
                if(i+1)//self.n==i//self.n:
                    #print("RIGHT")
                    newBoard=board[:]
                    newBoard[i],newBoard[i+1]=newBoard[i+1],newBoard[i]
                    if tuple(newBoard) not in self.seen:
                        heapq.heappush(self.queue,Node(newBoard,self.distance_heuristic(newBoard),newNumber+1,node))
                        self.seen.add(tuple(newBoard))

    '''
    Implementacja heurystyki misplaced
    @param board- aktualna plansza
    @return counter- liczba kafelków nie na swoich pozycjach
    '''

    def misplaced_heuristic(self,board):
        counter=0
        for i in range(self.m*self.n):
            #pomijamy pusty kafelek
            if(board[i]==self.n*self.m):
                continue
            if(board[i]!=i):
                #Jeśli kafelek nie na swoim miejscu, zwiększamy licznik
                counter=counter+1
        return counter
    '''
    Implementacja heurystyki distance
    @param board- aktualna plansza
    @return counter- suma odległości kafelków od finalnej pozycji
    '''

    def distance_heuristic(self,board):
        counter = 0
        for i in range(self.m*self.n):
            if board[i] == self.m*self.n:
                continue
            #pobierz finalne koordynaty
            row,column=self.Distance(board[i])
            #liczymy bezwzględne różnice i dodajemy do licznika
            counter=counter+abs(row-(i//self.n))+abs(column-(i%self.m))
        #print(counter)
        return counter



    '''
    Implementacja heurystyki linear
    @param board- aktualna plansza
    @return counter- suma odległości kafelków od finalnej pozycji z uwzględnieniem konfliktów liniowych
    '''
    def linear_heuristic(self,board):
        manhattan=self.distance_heuristic(board)
        conflict=0

        #Dwie osobne pętle- dla wierszy i kolumn
        for row in range(self.n):
            for i in range(self.m):
                for j in range(i+1,self.m):
                    #pomijamy pusty kafelek
                    if(board[row*self.m+i]!= self.m*self.n and board[row*self.m+j]!=self.m*self.n):
                        #Sprawdzenie warunku "przeszkadzania"
                        if(board[row*self.m+i] > board[row*self.m+j]):
                            #Pobranie finalnych koordynatów i sprawdzenie, czy znajdują się
                            #w tym samym rzędzie co aktualnie znajduje się dany numer
                            row_destination_i,_=self.Distance(board[row*self.m+i])
                            row_destination_j,_=self.Distance(board[row*self.m+j])
                            if(row_destination_i==row and row_destination_j==row):
                                conflict=conflict+1
        #Sytuacja analogiczna
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



    '''
    Funkcja obliczająca spodziewane końcowe położenie danego numeru
    @param number- numer dla której szulamy finalne położenie
    @return first,second- odpowiednio rząd i kolumna, w której finalnie powinien znaleźć się podany numer
    '''
    def Distance(self,number):
        #Dzielimy na wiersze
        first=number//self.n
        second=0
        #Dzielimy na kolumny
        if(number%self.n==0):
            first=first-1
            second=self.m-1
        else:
            second=number%self.n-1
        return first,second


    '''
    Funkcja odpowiedzialna za inicjalizację obiektu klasy Fifteen
    @param n- wysokość planszy
    @param m- szerokośc planszy
    '''
    def __init__(self,n,m):
        self.n=n
        self.m=m
        #Zmienna przechowująca planszę
        self.board=self.makePermutation()
        #Zmienna przechowująca odwiedzone stany w formie zbioru
        self.seen=set()
        #Kolejka priorytetowa, wykorzystana biblioteka heapq
        self.queue=[]
        #Zmienna przechowująca numer ruchu (zagłębienie w grafie)
        self.moveNumber=0

    #Funkcja odpowiedzialna za prezentacje obiektu klasy Fifteen
    def __str__(self):
        return self.Printer()


#Klasa odpowiedzialna za reprezentację pojedynczego stanu
class Node:

    '''
    Funkcja odpowiedzialna za inicjalizację obiektu klasy Node
    @param board- plansza
    @param functionValue- wartość funkcji heurystycznej
    @param moveNumber- numer ruchu (zagłębienie w grafie)
    @param previous- poprzedni stan
    '''
    def __init__(self,board,functionValue,moveNumber,previous):
        self.board=board
        self.functionValue=functionValue
        self.moveNumber=moveNumber
        self.previous=previous


    '''
    Funkcja odpowiedzialna za przejrzyste przedstawienie planszy
    @return result- reprezentacja planszy
    '''
    def Printer(self):
        result = ""
        for i in range(len(self.board)):
            result += f"{self.board[i]}" + ("\n" if i % 4 == 3 else " | ")
        result=result+"Move number: "+str(self.moveNumber)+"\n"
        return result

    #Przeciążenie operatora porównywania, niezbędne dla kolejki priorytetowej
    #@return porównane dwa obiekty typu Node
    def __lt__(self, other):
        return self.functionValue +self.moveNumber < other.functionValue + other.moveNumber


    #Funkcja odpowiedzialna za prezentacje obiektu klasy Fifteen
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
#12 
board=[16,7,1,4,3,10,11,8,5,15,14,6,2,13,9,12]
distance_heruistic: Visited:55523, Moves:38, Time:4.64s
linear_heuristic: Visited:28150, Moves:38, Time:7.43s

'''