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
