# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:00:02 2020

@author: soug9
"""

########## 가장 큰 정사각형 찾기 ##########

# 효율성 0점
def solution(board):
    
    h = len(board)
    w = len(board[0])
    
    for i in range(min(w,h), 0, -1) :
        for j in range(0, h-i+1) :
            for k in range(0, w-i+1) :
                if [b[k:k+i] for b in board[j:j+i]] == square :
                    return i*i
    
    return 0

# 정답
def solution(board) :
    
    if 1 not in sum(board, []) :
        return 0
    
    h = len(board)
    w = len(board[0])
    
    s = 1
    for i in range(1, h) :
        for j in range(1, w) :
            if board[i][j] == 1 :
                board[i][j] += min(board[i-1][j], min(board[i-1][j-1], board[i][j-1]))
                s = max(s, board[i][j])
                
    return s*s

board = [[0]] #0 test8
board = [[1]] #1 test1
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	# 9
board = [[0,0,1,1],[1,1,1,1]] # 4

solution(board)



########## 올바른 괄호 ##########

def solution(s):

    q = list()
    
    for ss in s :
        if ss == '(' :
            q.append(ss)
        else :
            if len(q) != 0 :
                q.pop()
            else :
                return False
                
    if len(q) != 0 :
        return False
    
    return True
    
s = "()()" # true
s = "(())()" # true
s = ")()("	# false
s = "(()("	# false

solution(s)



########## 다음 큰 숫자 ##########

'''
* 10진수 -> 2진수 : bin(n)

* 2진수 -> 10진수 : int(b,2) 

* 문제 접근
1. n을 2진수로 변환
2. 2진수로 변환한 n에 '01'이 포함될 경우 : 가장 오른쪽에 있는 01의 자리를 서로 바꿈
3. 그 외 : 가장 앞 자리의 1을 대신 10을 넣음
4. 2와 3에서 바꿔준 수의 자리 이후에 등장하는 숫자들을 재배치 : 1은 오른쪽, 0은 왼쪽으로
5. 2진수를 다시 10진수로 변환
'''


def solution(n):

    # 1
    binary = bin(n)[2:]
    
    #2   
    if '01' in binary :
        i = len(binary) - binary[::-1].index('10') -2
        binary = list(binary)
        binary[i], binary[i+1] = '1', '0'
      
    #3
    else :
        binary = ['1','0'] + list(binary[1:])
        i = 0
      
    #4
    len_1 = len([j for j in binary[i+2:] if j=='1'])
    binary[i+2:] = ['0'] * (len(binary[i+2:]) - len_1) + ['1'] * len_1  

    binary = ''.join(binary)

    #5        
    answer = int(binary, 2)
    
    return answer

# 3
n = 78	# 1001110 -> 1010011 83
n = 5 # 101 -> 110 6

# 4
n = 15	# 1111 -> 10111 23
n = 6 # 110 -> 1001 9
n = 2 # 10 -> 100 4
n = 1 # 1 -> 10 2

solution(n)



########## 땅따먹기 ##########

def solution(land):
    
    import copy
    
    def f(row, myland) :
        
        print(row, myland)
        
        
        if row == len(myland) :
            nonlocal land_size
            land_size.append(-sum([l[0] for l in myland]))
            
        else :
            newland = copy.deepcopy(myland)
            
            b_first = heapq.heappop(myland[row-1])
            first = heapq.heappop(myland[row])
            
            if b_first[1] == first[1] :
                b_second = heapq.heappop(myland[row-1])
                second = heapq.heappop(myland[row])
                
                if b_first[0] + second[0] == first[0] + b_second[0] :
                    
                    # row-1번째 값이 양보
                    newland[row-1] = b_first
                    newland[row] = second
                    f(row+1, newland)
                    
                    # row번째 값이 양보
                    newland[row-1] = first
                    newland[row] = b_second
                    f(row+1, newland)
                
                else :
                    newland[row-1] = b_first if b_first[0] + second[0] < first[0] + b_second[0] else first
                    newland[row] = second if b_first[0] + second[0] < first[0] + b_second[0] else b_second
                    f(row+1, newland)
                
            else :
                newland[row-1] = b_first
                newland[row] = first
                f(row+1, newland)
    
    # end of inner function
    
    import heapq
    
    myland = list()
    for i, row in enumerate(land) :
        hq = list()
        for j, r in enumerate(row) :
            heapq.heappush(hq, [-r,j])
        myland.append(hq)
        
    land_size = list()
    f(1, myland)
       
    answer = max(land_size)
    
    return answer


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	#16
land = [[1,2,3,5],[5,6,7,9],[1,1,4,1]]	#16
land = [[1,1,1,1]] #3
land = [[9, 5, 2, 3], [9, 8, 6, 7], [8, 9, 7, 1], [100, 9, 8, 1]]

solution(land)





























